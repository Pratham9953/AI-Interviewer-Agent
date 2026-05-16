from pydantic import BaseModel,Field
from typing import List,Optional
class FocusArea(BaseModel): skill:str;weight:int;question_count:int;difficulty:str
class EvaluationCriterion(BaseModel): name:str;weight:int;description:str
class JDAnalysisOutput(BaseModel): role_title:str;seniority:str;required_skills:List[str];responsibilities:List[str];interview_focus_areas:List[str];difficulty_level:str
class InterviewPlanOutput(BaseModel): total_questions:int;focus_areas:List[FocusArea];evaluation_criteria:List[EvaluationCriterion]
class InterviewQuestionOutput(BaseModel): question:str;skill:str;difficulty:str;expected_signals:List[str];follow_up_strategy:str
class AnswerScoreOutput(BaseModel): technical_accuracy:int=Field(ge=0,le=10);clarity:int=Field(ge=0,le=10);depth:int=Field(ge=0,le=10);relevance:int=Field(ge=0,le=10);confidence:int=Field(ge=0,le=10);overall_score:float=Field(ge=0,le=10);red_flags:List[str];missing_points:List[str];feedback:str;follow_up_needed:bool;follow_up_question:Optional[str]=None
class SkillScore(BaseModel): skill:str;score:float;feedback:str
class FinalReportOutput(BaseModel): overall_score:float;recommendation:str;strengths:List[str];weaknesses:List[str];skill_scores:List[SkillScore];communication_feedback:str;technical_feedback:str;improvement_plan:List[str];summary:str
