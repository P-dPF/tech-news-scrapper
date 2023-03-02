from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from tests.reading_plan.news_mock import NEWS
from unittest.mock import patch
import pytest


def mock_find_news():
    return NEWS


reading_plan_mock = {
    "readable": [
        {
            "unfilled_time": 5,
            "chosen_news": [
                ("noticia_5", 1),
                ("noticia_6", 1),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [("noticia_7", 7)],
        },
        {
            "unfilled_time": 2,
            "chosen_news": [("noticia_9", 5)],
        },
    ],
    "unreadable": [
        ("noticia_8", 8),
    ],
}


def test_reading_plan_group_news():
    mocked_news = mock_find_news()
    with patch.object(
        ReadingPlanService, "_db_news_proxy", return_value=mocked_news
    ):
        reading_plan = ReadingPlanService().group_news_for_available_time(7)

    print(reading_plan)
    assert reading_plan == reading_plan_mock

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService().group_news_for_available_time(0)
