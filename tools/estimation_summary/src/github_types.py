from dataclasses import dataclass

# These types are made for business logic. They may not match the actual
# GitHub API types exactly.

@dataclass
class SingleSelectFieldOption:
    """
    Projects can have custom fields that are single select fields.
    This class represents one of the options for a single select field.
    e.g. "High" or "Low" for a "Priority" field.
    """
    color: str
    description: str
    descriptionHTML: str
    id: str
    name: str
    nameHTML: str

@dataclass
class SingleSelectField:
    """
    Projects can have custom fields that are single select fields.
    e.g. "Priority" field (SingleSelectField) with options "High", "Medium",
    "Low" (SingleSelectFieldOptions).
    """
    id: str
    name: str
    options: list[SingleSelectFieldOption]

@dataclass
class Issue:
    """
    Note: this currently assumes that an issue is in exactly one project.
    Theoretically custom fields could be different in different projects!
    """
    id: int
    title: str
    url: str
    closed: bool
    milestone: str | None
    custom_fields: dict[str, str]
