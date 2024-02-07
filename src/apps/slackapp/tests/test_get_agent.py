from slackapp.utils import get_agent

from sherpa_ai.actions import ArxivSearch, GoogleSearch
from sherpa_ai.agents.qa_agent import QAAgent
from sherpa_ai.test_utils.data import get_file_path


def test_get_agent(get_file_path):  # noqa: F811
    config_filename = get_file_path(__file__, "test_get_agent.yaml")
    agent = get_agent(config_filename)

    assert agent is not None
    assert type(agent) is QAAgent

    assert len(agent.actions) == 2
    assert type(agent.actions[0]) is ArxivSearch
    assert type(agent.actions[1]) is GoogleSearch