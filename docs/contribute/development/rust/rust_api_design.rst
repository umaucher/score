Rust API design guidelines
##########################

.. document:: Rust API design guidelines
   :id: doc__rust_api_design
   :status: draft

Preface
=======

This document describes how public Rust APIs shall be designed in the S-CORE context. While these guidelines canalso be
beneficial for private APIs, following them also inside a single module is reommended to improve the code consistency
and also benefit from the perks it gives to the code.

Writing Mockable Rust Code
==========================

Mockable Rust code is a design pattern that emphasizes testability by expressing public APIs in terms of traits. This
approach allows developers to swap out real implementations with mock implementations during testing, enabling
controlled and predictable behavior for unit tests. By adhering to this pattern, you can isolate components under test
and avoid dependencies on external systems or complex logic.

Why Traits Enable Mocking
-------------------------

In Rust, traits define shared behavior that can be implemented by multiple types. When public APIs are expressed as
traits, you can provide one implementation for the real use case and another for testing purposes. During testing, a
mock struct (often created using crates like ``mockall``) can simulate the behavior of the real implementation, allowing
you to test your code in isolation. The mock struct may also be provided by the provider of the API so that users do not
need to reinvent the wheel by providing yet another mock implementation.

Below you will find an example of naive coding that is difficult to test because it directly depends on a concrete
implementation:

.. code-block:: rust

    pub struct RealDataFetcher;

    impl RealDataFetcher {
        pub fn fetch_data(&self, key: &str) -> String {
            format!("Real data for key: {}", key)
        }
    }

    pub struct DataProcessor {
        fetcher: RealDataFetcher,
    }

    impl DataProcessor {
        pub fn new(fetcher: RealDataFetcher) -> Self {
            Self { fetcher }
        }

        pub fn process(&self, key: &str) -> String {
            let data = self.fetcher.fetch_data(key);
            format!("Processed: {}", data)
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn test_data_processor() {
            let fetcher = RealDataFetcher;
            let processor = DataProcessor::new(fetcher);

            let result = processor.process("test_key");

            assert_eq!(result, "Processed: Real data for key: test_key");
        }
    }

The ``DataProcessor`` directly depends on ``RealDataFetcher``, making it impossible to substitute a mock implementation.
Tests cannot control or predict the behavior of ``fetch_data``, leading to reliance on real data or external systems.
This coupling makes the code harder to test and less flexible.

The solution to these issues is a refactoring that extracts the API from teh implementation by means of a trait and using
a system part by means of that trait instead of a direct dependency, as above.

Providing the implementation for this trait can be done in two different ways in Rust: Static dispatch by means of generic
parameters or dynamic dispatch by handing over references to trait objects. The following paragraphs will give examples
for both methods.

Positive Example: Mockable Code with Static Dispatch
----------------------------------------------------

Below is an example of mockable Rust code using the ``mockall`` crate and static dispatch:

.. code-block:: rust

    pub trait DataFetcher {
        fn fetch_data(&self, key: &str) -> String;
    }

    pub struct RealDataFetcher;

    impl DataFetcher for RealDataFetcher {
        fn fetch_data(&self, key: &str) -> String {
            format!("Real data for key: {}", key)
        }
    }

    pub struct DataProcessor<T: DataFetcher> {
        fetcher: T,
    }

    impl<T: DataFetcher> DataProcessor<T> {
        pub fn new(fetcher: T) -> Self {
            Self { fetcher }
        }

        pub fn process(&self, key: &str) -> String {
            let data = self.fetcher.fetch_data(key);
            format!("Processed: {}", data)
        }
    }

    #[cfg(test)]
    mockall::mock! {
        pub DataFetcher {}

        impl DataFetcher for DataFetcher {
            fn fetch_data(&self, key: &str) -> String;
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use mockall::predicate::*;

        #[test]
        fn test_data_processor_with_mock() {
            let mut mock_fetcher = MockDataFetcher::new();
            mock_fetcher
                .expect_fetch_data()
                .with(eq("test_key"))
                .returning(|_| "Mock data".to_string());

            let processor = DataProcessor::new(mock_fetcher);
            let result = processor.process("test_key");

            assert_eq!(result, "Processed: Mock data");
        }
    }

Positive Example: Mockable Code with Dynamic Dispatch
-----------------------------------------------------

Here’s an example using dynamic dispatch with a ``&mut dyn`` reference:

.. code-block:: rust

   #[cfg_attr(test, mockall::automock)]
    pub trait DataFetcher {
        fn fetch_data(&self, key: &str) -> String;
    }

    pub struct RealDataFetcher;

    impl DataFetcher for RealDataFetcher {
        fn fetch_data(&self, key: &str) -> String {
            format!("Real data for key: {}", key)
        }
    }

    pub struct DataProcessor<'a> {
        fetcher: &'a mut dyn DataFetcher,
    }

    impl<'a> DataProcessor<'a> {
        pub fn new(fetcher: &'a mut dyn DataFetcher) -> Self {
            Self { fetcher }
        }

        pub fn process(&self, key: &str) -> String {
            let data = self.fetcher.fetch_data(key);
            format!("Processed: {}", data)
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use mockall::predicate::*;

        #[test]
        fn test_data_processor_with_dyn_dispatch() {
            let mut mock_fetcher = MockDataFetcher::new();
            mock_fetcher
                .expect_fetch_data()
                .with(eq("test_key"))
                .returning(|_| "Mock data".to_string());

            let processor = DataProcessor::new(&mut mock_fetcher);
            let result = processor.process("test_key");

            assert_eq!(result, "Processed: Mock data");
        }
    }


.. note:: Instead of explicitly implementing the mock as in the above example, we now use ``automock`` to generate the
          mock implementation. While this isn't always possible, it is very convenient in most cases where the macro
          works.

Pros and Cons of Static vs Dynamic Dispatch
-------------------------------------------

**Static Dispatch:**

* **Pros:**

  * Compile-time type checking ensures safety and performance.
  * No runtime overhead for method calls.
  * Easier to optimize by the compiler.

* **Cons:**

  * Requires generics, which can increase code complexity and binary size.
  * May lead to code duplication if many types implement the same trait.

**Dynamic Dispatch:**

* **Pros:**

  * Allows runtime polymorphism, making the code more flexible.
  * Avoids generics, reducing code complexity and binary size.

* **Cons:**

  * Slight runtime overhead due to vtable lookups.
  * Less compile-time type safety compared to static dispatch.

Conclusion
----------

By designing APIs around traits, you can create mockable Rust code that is easier to test and maintain. Both static and
dynamic dispatch have their use cases, and the choice depends on the specific requirements of your project. Static
dispatch is ideal for performance-critical applications, while dynamic dispatch offers flexibility and simplicity. Avoid
direct dependencies on concrete implementations to prevent testing difficulties and tightly coupled code.
