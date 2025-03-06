from dataclasses import dataclass, field

import github_types as github_types
import queries.get_projectv2_issues
import queries.set_project_description
from github_basics import GitHubClient_Basic


@dataclass
class ProjectData:
    field_ids: dict[str, str] = field(default_factory=dict)
    """field_name -> field_id"""

    single_select_fields: dict[str, dict[str, str]] = field(default_factory=dict)
    """field_name -> option_name -> option_id"""


class GitHubClient(GitHubClient_Basic):
    def __init__(self, org: str, token: str | None = None):
        """
        Hint: you *must* use this class as a context manager.

        Args:
          token: will default to the GITHUB_TOKEN environment variable if not provided.
        """
        super().__init__(org, token)

        self.project_data = ProjectData()

    async def issues_from_project(self, project_number: int):
        """
        Get all issues within the project.

        Warning: result is cached for 1 hour.
        Changes to GitHub will not be reflected.
        """
        return await queries.get_projectv2_issues.run_query(self, project_number)

    async def set_project_description(self, project_number: int, readme: str):
        """Will return a dict with the project name and new readme."""

        await queries.set_project_description.run_mutation(
            client=self,
            org="eclipse-score",
            project_number=project_number,
            readme="\n".join(readme),
        )
