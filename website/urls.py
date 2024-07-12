from django.urls import path
from django.conf.urls.static import static
from .import views
from django.conf import settings

urlpatterns = [

    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('user_panel/', views.user_panel, name="user_panel"),
    path('data_coll/', views.data_coll, name="data_coll"),
    path('dash/', views.dash, name="dash"),
    path('disruption/', views.disruption, name="disruption"),
    path('data_analysis/', views.data_analysis, name="analysis"),
    path('team/', views.team, name="team"),
    path('data_coll/infrastructure/', views.infrastructure, name="infrastructure"),
    path('data_coll/education/', views.education, name="education"),
    path('data_coll/finance/', views.finance, name="finance"),
    path('data_coll/compliance/', views.compliance, name="compliance"),
    path('data_coll/community/', views.community, name="community"),
    path('project/', views.project, name="project"),
    path('data_repo', views.repository, name="repository"),
    path('submit/', views.submit, name="submit"),


    path('strategies/financial_planning/', views.financial_planning, name="financial_planning"),
    path('strategies/continuous_improvement_assessment/', views.continuous_improvement_assessment, name="continuous_improvement_assessment"),
    path('strategies/', views.strategies, name="strategies"),
    path('strategies/workforce_planning/', views.workforce_planning, name="workforce_planning"),
    path('strategies/technology_integration/', views.technology_integration, name="technology_integration"),
    path('strategies/mental_health_support_service/', views.mental_health_support_service, name="mental_health_support_service"),
    path('strategies/blended_learning/', views.blended_learning, name="blended_learning"),
    path('strategies/safety_measure/', views.safety_measure, name="safety_measure"),
    path('strategies/comprehensive_health_safety_measure/', views.comprehensive_health_safety_measure, name="comprehensive_health_safety_measure"),
    path('strategies/program_curriculum_review_update/', views.program_curriculum_review_update, name="program_curriculum_review_update"),
    path('strategies/research_experiment_standardization/', views.research_experiment_standardization, name="research_experiment_standardization"),
    path('strategies/professional_development_plan/', views.professional_development_plan, name="professional_development_plan"),
    path('strategies/enrollment_initiative/', views.enrollment_initiative, name="enrollment_initiative"),
    path('strategies/budget_optimization/', views.budget_optimization, name="budget_optimization"),
    path('strategies/financial_auditing/', views.financial_auditing, name="financial_auditing"),
    path('strategies/cash_flow_analysis/', views.cash_flow_analysis, name="cash_flow_analysis"),
    path('strategies/compliance_management_framework/', views.compliance_management_framework, name="compliance_management_framework"),
    path('strategies/transparent_governance_framework/', views.transparent_governance_framework, name="transparent_governance_framework"),
    path('strategies/mission_driven_policy_alignment/', views.mission_driven_policy_alignment, name="mission_driven_policy_alignment"),
    path('strategies/security_measure/', views.security_measure, name="security_measure"),
    path('strategies/community_engagement_initiative/', views.community_engagement_initiative, name="community_engagement_initiative"),
    path('strategies/accommodation_optimization/', views.accommodation_optimization, name="accommodation_optimization"),
    path('strategies/strategic_recruitment/', views.strategic_recruitment, name="strategic_recruitment"),
    path('strategies/workflow_analysis/', views.workflow_analysis, name="workflow_analysis"),
    path('strategies/digitization/', views.digitization, name="digitization"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

