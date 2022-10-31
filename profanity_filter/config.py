from typing import List, Optional

from pydantic import BaseModel

from profanity_filter.types_ import AnalysisType, Language


# noinspection PyTypeChecker
class Config(BaseModel):
    analyses: List[AnalysisType] = list(AnalysisType)
    cache_redis_connection_url: Optional[str] = None
    censor_char: str = '*'
    censor_whole_words: bool = True
    languages: List[Language] = ['en_core_web_sm']
    max_relative_distance: float = 0.34


DEFAULT_CONFIG = Config()
