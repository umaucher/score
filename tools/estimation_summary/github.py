import sys
from collections import defaultdict
from dataclasses import dataclass, field

# sys.path.insert(0, ".")
import github_types as github_types
import query_projectv2_issues
import query_projectv2_single_select_fields
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
        return await query_projectv2_issues.run_query(self, project_number)

    async def single_select_fields_in_project(self, project_number: int):
        """
        Get all single select fields within the project.

        Warning: result is cached for 1 hour.
        Changes to GitHub will not be reflected.
        """
        return await query_projectv2_single_select_fields.run_query(self, project_number)

