from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Disruptor
from .models import Facilities, Academic, Finance, Administrative, Social
from .models import Team
from django.urls import reverse
from .models import Document
from .forms import DocumentForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('user_panel')
    else:

        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account created for ' +user)
               return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('user_panel')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect(reverse('admin:index'))  # Redirect to Jazzmin admin panel
                else:
                    return redirect('user_panel')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def user_panel(request):
     return render(request, 'dashboard.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def data_coll(request):
    return render(request, 'data_coll.html')

def dash(request):
    return render(request, 'dashboard.html')

def disruption(request):
    disruptor = Disruptor.objects.all()
    context = {'disruptors': disruptor}
    return render(request, 'disruption.html', context)
    #return redirect("https://stremlitmodel1.streamlit.app")

def data_analysis(request):
    return render(request, 'data_analysis.html')

def team(request):
    member = Team.objects.all()
    context = {'members':member}
    return render(request, 'team.html', context)

def infrastructure(request):
    return render(request, 'infrastructure.html')
def education(request):
    return render(request, 'education.html')
def finance(request):
    return render(request, 'finance.html')
def compliance(request):
    return render(request, 'compliance.html')
def community(request):
    return render(request, 'community.html')
def project(request):
    return render(request, 'project.html')

def repository(request):
    document = Document.objects.all()
    context = {'documents':document}
    return render(request, 'data_repository.html', context)

def strategies(request):
    return render(request, 'strategies.html')
def continuous_improvement_assessment(request):
    return render(request, 'continuous_improvement_assessment.html')
def financial_planning(request):
    return render(request, 'financial_planning.html')
def workforce_planning(request):
    return render(request, 'workforce_planning.html')
def technology_integration(request):
    return render(request, 'technology_integration.html')
def mental_health_support_service(request):
    return render(request, 'mental_health_support_service.html')
def blended_learning(request):
    return render(request, 'blended_learning.html')
def safety_measure(request):
    return render(request, 'safety_measure.html')
def comprehensive_health_safety_measure(request):
    return render(request, 'comprehensive_health_safety_measure.html')
def program_curriculum_review_update(request):
    return render(request, 'program_curriculum_review_update.html')
def digitization(request):
    return render(request, 'digitization.html')
def research_experiment_standardization(request):
    return render(request, 'research_experiment_standardization.html')

def professional_development_plan(request):
    return render(request, 'professional_development_plan.html')

def enrollment_initiative(request):
    return render(request, 'enrollment_initiative.html')

def budget_optimization(request):
    return render(request, 'budget_optimization.html')

def financial_auditing(request):
    return render(request, 'financial_auditing.html')

def cash_flow_analysis(request):
    return render(request, 'cash_flow_analysis.html')

def compliance_management_framework(request):
    return render(request, 'compliance_management_framework.html')

def transparent_governance_framework(request):
    return render(request, 'transparent_governance_framework.html')

def mission_driven_policy_alignment(request):
    return render(request, 'mission_driven_policy_alignment.html')

def security_measure(request):
    return render(request, 'security_measure.html')

def community_engagement_initiative(request):
    return render(request, 'community_engagement_initiative.html')

def accommodation_optimization(request):
    return render(request, 'accommodation_optimization.html')

def strategic_recruitment(request):
    return render(request, 'strategic_recruitment.html')

def workflow_analysis(request):
    return render(request, 'workflow_analysis.html')
def submit(request):
    return render(request, 'gpt_response.html')



import os
import re 
from openai import OpenAI
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Fetch API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

print(f"Views: Retrieved API key: {openai_api_key}")  # Debug print

try:
    client = OpenAI(api_key=openai_api_key)
    print("OpenAI client initialized successfully.")
except Exception as e:
    print(f"Error initializing OpenAI client: {str(e)}")

def interpret_score(score):
    if score >= 18:
        return "The problem has a significant impact on the organization. Immediate and comprehensive measures are required."
    elif 12 <= score < 18:
        return "The problem has a moderate impact on the organization. Consider taking targeted actions to mitigate the effects."
    elif 8 <= score < 12:
        return "The problem has a minor impact on the organization. Monitor the situation and take preventive measures."
    else:
        return "The problem has a negligible impact on the organization. No immediate action is required, but continue to monitor."

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        # Extract form data
        form_data = {
            'question1': request.POST.get('question1'),
            'question2': request.POST.get('question2'),
            'question3': request.POST.get('question3'),
            'question4': request.POST.get('question4'),
            'question5': request.POST.get('question5'),
            'question6': request.POST.get('question6'),
            'question7': request.POST.get('question7'),
            'question8': request.POST.get('question8'),
            
        }

        # Extract form heading
        form_heading = request.POST.get('form_heading')

       # Define weights for answers
        answer_weights = {
       'not_at_all': 0,
       'slightly': 1,
       'a_few_areas': 1,
       'somewhat': 1,
       'a_few_resources': 1,
       'rarely': 1,
       'a_few': 1,
       'a_few_times': 1,
       'moderately': 2,
       'several_areas': 2,
       'occasionally': 2,
       'several_resources': 2,
       'most_resources': 3,
       'considerably': 2,
       'several': 2,
       'several_times': 2,
       'significantly': 3,
       'most_areas': 3,
       'extensively': 3,
       'frequently': 3,
       'severely': 3,
       'many': 3,
       'many_areas': 3,
       'many_times': 3,
       'many_issues': 3,
       'greatly': 3,
       'none': 0,
       'major_issues': 4,
       
       }


        # Calculate the scores
        score = sum(answer_weights[answer] for answer in form_data.values())

        # Interpret the score
        score_interpretation = interpret_score(score)

        # Fetch data from the Disruptor model
        disruptors = Disruptor.objects.all()
        
        # Initialize response text
        response_text = ""

        # Fetch data from the Facilities model
        facilities = Facilities.objects.all()

        # Create a dictionary to store facility data
        facility_data = {
        "classrooms": ", ".join(f.classrooms for f in facilities if f.classrooms),
        "library": ", ".join(f.library for f in facilities if f.library),
        "laboratory": ", ".join(f.laboratory for f in facilities if f.laboratory),
        "accomodation": ", ".join(f.accomodation for f in facilities if f.accomodation),
        "playgrounds": ", ".join(f.playgrounds for f in facilities if f.playgrounds),
        "online_resources": ", ".join(f.online_resources for f in facilities if f.online_resources),
        "health_facilities": ", ".join(f.health_facilities for f in facilities if f.health_facilities),
        }

        socials = Social.objects.all()
        social_data = {
        "sport": ", ".join(s.sport for s in socials if s.sport),
        } 

        academics = Academic.objects.all()
        academic_data = {
        "colleges": ", ".join(a.college for a in academics if a.college),
        "programs": ", ".join(a.programs for a in academics if a.programs),
        "enrollment_rates": ", ".join(str(a.enrollment_rate) for a in academics if a.enrollment_rate),
        }


        finances = Finance.objects.all()
        finance_data = {
        "colleges": ", ".join(a.college for a in academics if a.college),
        "program": ", ".join(a.program for a in finances if a.program),
        "tuition_fee": ", ".join(f.tuition_fee for f in finances if f.tuition_fee),
        }

        administratives = Administrative.objects.all()
        administrative_data = {
        "policies": ", ".join(a.policy for a in administratives if a.policy),
        }

        # Define prompts with placeholders for facility data
        prompts = {
            "Learning environment": [
               f"Given the {score_interpretation}, in your response, don't forget to mention the availability of internal facilities such as libraries ({facility_data['library']}), "
               f"labs ({facility_data['laboratory']}), and classrooms ({facility_data['classrooms']}) found in various colleges across the University of Dodoma. "
               f"Encourage their optimization to solve the given problem. Additionally, emphasize the usage of external online learning tools such as Google, YouTube, ChatGPT, "
               f"Google Classroom, Zoom Meeting, and other similar platforms that can promote remote teaching and learning. "
               f"The response should be relevant to the affected aspects in the given context. "
               f"Also, ensure your response aligns with the Guidelines for Online and Blended Delivery Modes of Courses for University Institutions in Tanzania."
            ],
            "Physical Health and safety":[
               f"Given the {score_interpretation}, consider the physical health challenges faced by the organization and suggest appropriate measures to improve health and safety. "
               f"Consider the impact of physical health on remote teaching and learning and propose suitable solutions. "
               f"In your response, mention the importance of sports and games ({social_data['sport']}) to enhance health and safety."


            ],
            "Mental Health and Emotional well being":[
                f"Given the {score_interpretation}, consider the current mental health and emotional well-being of students, staff, and the community. Propose measures to address mental health needs and suggest ways to promote emotional well-being.",
                f"In your response, don't forget to mention some of the mental health facilities and hospitals in Tanzania such as Mirembe Hospital, Benjamin Mkapa Hospital, Aga Khan Hospital, and other therapy facilities in Tanzania.",
                f"Discuss the importance of accessible mental health services and propose strategies to improve access to counseling and psychological support within the institution.",
                f"Evaluate the role of mental health awareness programs in reducing stigma and promoting a supportive environment for seeking help.",
                f"Propose the implementation of regular mental health check-ins and workshops to equip students and staff with coping strategies and stress management techniques."
            ],
            "Educational programs and curriculum": [
           f"Given the {score_interpretation}, discuss the current educational programs and curriculum in place, ensuring the response is relevant to the given context and the affected aspects.",
    f"Additionally in your response, emphasize some of the colleges ({academic_data['colleges']}) and programs ({academic_data['programs']}) offered at the University of Dodoma.",
    f"Evaluate the alignment of the curriculum with the Tanzania University Guidebooks for both undergraduate and postgraduate programs, highlighting areas of strength and opportunities for improvement.",
    f"Propose strategies for integrating innovative teaching methods and technologies to enhance the learning experience and ensure curriculum relevance in the evolving educational landscape.",
    f"Discuss the importance of regular curriculum reviews and updates to maintain academic excellence and meet the changing needs of students and the job market.",
    f"Highlight the role of interdisciplinary programs and collaborations between colleges in fostering a well-rounded education and addressing complex societal challenges.",
    f"Recommend measures to promote active learning and student engagement through practical experiences, research opportunities, and industry partnerships.",
    f"Also, ensure your response aligns with the Guidelines for Online and Blended Delivery Modes of Courses for University Institutions in Tanzania."
],

            "Research and Experiments":[
                f"Given the {score_interpretation}, consider the current state of research facilities and the impact on ongoing experiments. Propose measures to support remote research activities and ensure the continuity of experiments."
                f"In your response don't forget to mention ({facility_data['online_resources']}),({facility_data['library']}) and  ({facility_data['laboratory']}) "
                 f"Also, ensure your response aligns with the Guidelines for Online and Blended Delivery Modes of Courses for University Institutions in Tanzania."
            ],
            "Students Enrollment":[
                f"Given the {score_interpretation}, consider the current enrollment trends and propose strategies to maintain or increase student enrollment during the disruption. Include suggestions for remote learning initiatives and outreach programs."
                f"In your response don't forget to mention ({academic_data['enrollment_rates']}) "           
            
            ],
            "Technology infrastructures":[
                f"Given the {score_interpretation}, address the current technology infrastructure in place and propose improvements to support remote teaching and learning. Consider the availability of internet access, devices, and online learning platforms."
                f"In your response don't forget to mention ({facility_data['online_resources']}),({facility_data['library']}) and  ({facility_data['classrooms']}) "
                f"Additionally, emphasize the usage of external technology infrastructures such as cloud based and other emerging technologies to promote remote teaching and learning "
                f"Also, ensure your response aligns with the Guidelines for Online and Blended Delivery Modes of Courses for University Institutions in Tanzania."
            ],
            "Access to resources":[
                f"Given the {score_interpretation}, suggest ways to improve access to resources necessary for effective learning, including digital libraries, online courses, and virtual labs."
                f"In your response don't forget to mention ({facility_data['online_resources']}),({facility_data['library']}) and  ({facility_data['classrooms']}) "
                f"Also, ensure your response aligns with the Guidelines for Online and Blended Delivery Modes of Courses for University Institutions in Tanzania."
            ],
            "Facilities safety":[
                 f"Given the {score_interpretation}, discuss the safety measures currently in place for facilities and propose additional measures to ensure the safety of students and staff.",
    f"Evaluate the existing protocols for maintaining safety in accommodation ({facility_data['accomodation']}) and suggest improvements or new measures to address potential risks.",
    f"Consider the safety measures in the library ({facility_data['library']}) and recommend strategies to enhance security, such as improved surveillance and emergency response plans.",
    f"Emphasize assessment the safety of classrooms ({facility_data['classrooms']}) and propose solutions to ensure a safe learning environment, including regular safety drills and updated emergency procedures.",
    f"Review the safety protocols in laboratories ({facility_data['laboratory']}) and suggest enhancements to protect against accidents, such as proper storage of hazardous materials and regular safety training for staff and students.",
    
           ],
    "Quality Assurance": [
    f"Given the {score_interpretation}, evaluate the current quality assurance processes and suggest improvements to maintain educational standards during remote learning.",
    f"In your response don't forget to mention ({facility_data['online_resources']}),({facility_data['library']}) and  ({facility_data['classrooms']}) "
    f"In your response, don't forget to mention the importance of online resources ({facility_data['online_resources']}), libraries ({facility_data['library']}), classrooms ({facility_data['classrooms']}), and laboratories ({facility_data['laboratory']}) in supporting quality education.",
    f"Assess the effectiveness of current quality assurance mechanisms in adapting to the challenges of remote learning and propose enhancements to ensure continuous improvement, emphasizing the role of libraries ({facility_data['library']}), classrooms ({facility_data['classrooms']}), and laboratories ({facility_data['laboratory']}).",
    f"Discuss the role of accreditation bodies and compliance with regulatory standards in maintaining the credibility and recognition of educational programs, supported by the online resources ({facility_data['online_resources']}) and other facilities.",
    f"Propose strategies for regular monitoring and evaluation of online teaching and learning processes, highlighting the use of online resources ({facility_data['online_resources']}), libraries ({facility_data['library']}), and laboratories ({facility_data['laboratory']}).",
    f"Highlight the importance of feedback from students, faculty, and other stakeholders in identifying areas for improvement, specifically in the utilization of libraries ({facility_data['library']}), classrooms ({facility_data['classrooms']}), and laboratories ({facility_data['laboratory']}).",
    f"Recommend measures to enhance faculty training and support to uphold high teaching standards in a remote learning environment, utilizing the available online resources ({facility_data['online_resources']}).",
   f"Also, ensure your response aligns with the Guidelines for Online and Blended Delivery Modes of Courses for University Institutions in Tanzania."
],


            "Students Accomodation":[
                f"Given the {score_interpretation}, consider the current state of student accommodation and propose solutions to address any issues related to housing and support for students."
                f"In your response don't forget to mention ({facility_data['accomodation']})) "
                f"Consider the impact of remote learning on accommodation needs and propose strategies to support students who may need to stay on campus or find alternative housing arrangements.",
                f"Discuss any policies or programs currently in place to assist students with accommodation and suggest improvements or new initiatives that could enhance their living conditions and overall well-being."
            ],   
            "Recruitment":[
                f"Given the {score_interpretation}, discuss the impact of the disruption on recruitment processes and propose strategies to attract and retain staff during this period at the university of Dodoma."
                f"Don't forget to mention various colleges ({academic_data['colleges']})"
                  f"Discuss the potential for leveraging technology and online platforms to facilitate recruitment and onboarding processes, ensuring that new staff can be integrated smoothly despite any disruptions.",
    f"Explore the importance of providing support and resources to new recruits, including professional development opportunities, to enhance their experience and retention at the university."
            ],
            "Governance structure":[
                f"Given the {score_interpretation}, evaluate the current governance structure and propose changes to enhance decision-making and management during the disruption. "
                f"Discuss the roles and responsibilities of key governance bodies and suggest improvements to ensure efficient and transparent decision-making. "
                f"Consider the impact of remote operations on governance and propose strategies to maintain effective communication and collaboration among stakeholders. "
                f"In your response, emphasize the importance of adhering to the university's policies and regulations, ensuring accountability and compliance."
            ],
            "Running cost":[
                f"Given the {score_interpretation}, provide recommendations on how to manage running costs effectively during the disruption. "
                f"Include cost-cutting measures and budget optimization strategies to ensure financial stability. "
                f"Discuss the impact of the disruption on operational expenses and propose ways to minimize unnecessary expenditures while maintaining essential services. "
                f"Consider the use of technology and automation to improve efficiency and reduce costs. "
                f"Evaluate potential areas for renegotiating contracts or finding alternative suppliers to lower expenses. "
                f"In your response, emphasize the importance of maintaining transparency and accountability in financial management."
            ],  
            "Cyber crime":[
                f"Given the {score_interpretation}, address the potential risks of cybercrime and propose measures to enhance cybersecurity and protect sensitive information."
                f"Assess the current cybersecurity infrastructure and identify any vulnerabilities that need to be addressed.",
                f"Propose strategies for increasing awareness and training among staff and students on recognizing and preventing cyber threats.",
    f"Recommend the implementation of advanced security technologies such as multi-factor authentication, encryption, and intrusion detection systems.",
    f"Suggest policies and protocols for handling sensitive information and responding to security breaches.",
    f"In your response, don't forget to mention the security of online resources ({facility_data['online_resources']}) and suggest measures to enhance their protection.",
    f"Discuss the importance of regular security audits and updates to the cybersecurity infrastructure.",
    f"Highlight the role of collaboration with cybersecurity experts and law enforcement agencies in preventing and addressing cybercrime.",
    f"Consider the impact of remote working and learning on cybersecurity and propose solutions to mitigate associated risks.",
    f"Recommend a comprehensive incident response plan to effectively manage and recover from cyber attacks."
            ],
            "Workforce planning and analysis":[
                f"Given the {score_interpretation}, discuss the current workforce planning and analysis processes and propose improvements to ensure optimal staff allocation and productivity.",
                f"Consider strategies for forecasting future workforce needs based on organizational goals and objectives.",
                f"In your response, include methods for identifying and addressing skill gaps within the workforce.",
                f"Discuss the importance of employee development and training programs in enhancing workforce capabilities.",
                f"Propose how to leverage data and analytics to make informed decisions about workforce planning and resource allocation.",
                f"Highlight the role of employee engagement and satisfaction in maintaining a productive and motivated workforce.",
                f"Suggest ways to improve the flexibility and adaptability of the workforce to meet changing organizational needs."
            ],
            "Social Connections and Community Engagement":[
f"Given the {score_interpretation}, evaluate the current state of social connections and community engagement within the organization. ",
    f"Propose strategies to strengthen social connections among students, staff, and the wider community during the disruption. ",
    f"Discuss the importance of community engagement in fostering a sense of belonging and support, particularly in challenging times. ",
    f"In your response, consider initiatives to enhance virtual and in-person community-building activities. ",
    f"Highlight the role of social media and online platforms in maintaining and promoting community engagement. ",
    f"Suggest ways to involve community partners and stakeholders in supporting the organization's goals and activities. ",
    f"Evaluate the impact of remote learning and working on social connections and propose measures to mitigate any negative effects. ",
    f"Discuss the importance of cultural, social, and recreational activities in promoting community well-being and engagement. ",
    f"Propose initiatives to recognize and celebrate the contributions of individuals and groups to community building. ",
    f"Recommend methods to gather feedback from the community to improve engagement strategies and address emerging needs. ",
    f"Consider the role of community engagement in enhancing the overall educational experience and fostering long-term relationships. "
            ],
            "Employee development and Training":[
                f"Given the {score_interpretation}, consider the impact on employee development and training programs and propose solutions to continue these initiatives remotely."
                f"Discuss the importance of continuous learning and development in maintaining a competitive workforce.",
                f"Propose strategies for delivering effective remote training sessions using various online platforms and tools.",
                f"Highlight methods for assessing the effectiveness of remote training programs and ensuring they meet learning objectives.",
                f"Consider ways to foster a culture of learning and development within the organization, even in a remote work environment.",
                f"Suggest approaches to personalize training programs to cater to individual employee needs and career goals.",
                f"Discuss the role of mentorship and coaching in employee development and how these can be adapted for remote settings.",
                f"Identify potential challenges in remote training and development and propose solutions to overcome them."
            ],
            "Tuition and fee setting":[
                 f"Given the {score_interpretation}, evaluate the current tuition and fee structure and propose adjustments to ensure affordability and accessibility during the disruption."
                 f"Analyze the financial impact of the current tuition and fee structure on students.",
                 f"Suggest alternative pricing models that could offer more flexibility and support for students facing financial difficulties.",
                 f"Consider the balance between maintaining the institution financial stability and providing affordable education.",
                 f"Propose strategies to communicate any changes in tuition and fees transparently to students and stakeholders.",
                 f"Evaluate the potential for implementing scholarships, grants, or payment plans to assist students financially.",
    f"Discuss the impact of remote learning on tuition and fees and propose adjustments to reflect changes in delivery mode.",
    f"Identify opportunities for cost savings that could be passed on to students to reduce financial burden.",
    f"Highlight the importance of engaging with student representatives and stakeholders in the decision-making process for tuition and fee adjustments."
    f"Also, ensure your response align with Undergraduate Admission Guidebooks."        
            ],
            "Administrative Functions":[
f"Given the {score_interpretation}, evaluate the current administrative functions and propose improvements to enhance efficiency and effectiveness during the disruption. "
    f"Discuss the impact of the disruption on various administrative processes such as student registration, record keeping, and staff management. "
    f"Propose the adoption of digital tools and platforms to streamline administrative tasks and reduce manual workload. "
    f"Consider the implementation of remote working policies and practices to ensure continuity of administrative operations. "
    f"In your response, highlight the importance of clear communication channels and regular updates to keep all stakeholders informed. "
    f"Recommend strategies for training and supporting administrative staff to adapt to new technologies and work practices. "
    f"Emphasize the need for data security and privacy measures in handling administrative information. "
    f"Propose methods to monitor and evaluate the effectiveness of administrative functions during the disruption."
            ],
            "Mission, Vision, and Values":[
f"Given the {score_interpretation}, assess how the current mission, vision, and values align with the organization's goals and objectives during the disruption. ",
    f"Discuss the importance of reaffirming the mission, vision, and values to maintain organizational focus and direction in challenging times. ",
    f"Propose strategies to communicate and reinforce the mission, vision, and values to all stakeholders, ensuring they remain a guiding force. ",
    f"Consider the role of the mission, vision, and values in decision-making processes and how they can inspire resilience and adaptability. ",
    f"Evaluate how the mission, vision, and values can support the organization's response to the disruption and its long-term recovery plans. ",
    f"In your response, highlight examples of how the organization has successfully upheld its mission, vision, and values during the disruption. ",
    f"Recommend initiatives to embed the mission, vision, and values into daily operations and organizational culture. ",
    f"Discuss the importance of aligning the mission, vision, and values with the needs and expectations of students, staff, and the wider community. ",
    f"Suggest ways to gather feedback from stakeholders to ensure the mission, vision, and values remain relevant and impactful. ",
    f"Propose methods to celebrate and recognize achievements that reflect the organization's commitment to its mission, vision, and values."
            ],
            "Debt":[
                f"Given the {score_interpretation}, address the current debt levels and propose strategies to manage and reduce debt during the disruption."
                f"Analyze the impact of the disruption on the organization's revenue streams and suggest alternative funding sources to mitigate debt accumulation.",
    f"In your response, consider the role of government aid and financial assistance programs in alleviating debt burdens.",
    f"Discuss the importance of maintaining transparent financial reporting and accountability to stakeholders in managing debt effectively.",
    f"Propose measures to optimize operational costs and improve financial efficiency to prevent further debt escalation.",
    f"Evaluate the potential benefits of debt restructuring or refinancing options to manage existing debt obligations more sustainably.",
    f"Consider the long-term financial planning and risk management strategies needed to ensure the organization remains financially stable post-disruption.",
    f"Highlight the importance of stakeholder engagement and communication in addressing debt challenges and securing support for debt reduction initiatives."
            ],
            "Budget allocation":[
                f"Given the {score_interpretation}, suggest various measures that can be implemented to effectively control budget allocation.",
                f"Consider strategies for prioritizing essential expenditures while identifying areas where costs can be reduced.",
                f"In your response, include methods for monitoring and evaluating budget performance to ensure financial efficiency.",
                f"Discuss the role of transparent reporting and accountability in maintaining a balanced budget.",
                f"Propose how to involve stakeholders in the budgeting process to ensure comprehensive financial planning and resource allocation."
            ],
            "Legal and Regulatory compliance":[
                f"Given the {score_interpretation}, evaluate the current legal and regulatory compliance measures within the organization and propose specific improvements to ensure adherence during the disruption.",
    f"In your response, consider the impact of remote operations on compliance requirements and suggest strategies to address any gaps.",
    f"Don't forget to mention key policies such as ({administrative_data['policies']}) and how they can be adapted or reinforced in the current context.",
    f"Also, consider the role of training and awareness programs in ensuring that staff are fully informed about compliance obligations during this period.",
    f"Highlight the importance of regular audits and monitoring to maintain compliance standards and propose how these can be effectively conducted remotely."
]
        
        }

        for disruptor in disruptors:
            # Check if the form heading matches the affected aspect
            if form_heading == disruptor.affected_aspect:
                # Get the prompt for the matching affected aspect
                prompt = prompts.get(form_heading, [f"Given the {score_interpretation}, provide recommendations."])[0]

                # Format the data for OpenAI API
                input_text = "\n".join([f"{key}: {value}" for key, value in form_data.items()])
                
                # Include the prompt in the input text
                input_text = f"{prompt}\n{input_text}"

                # Call OpenAI API
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a main advisor for the University of Dodoma located in Tanzania with knowledge about various aspects that affect learning and development of students and university at large. Provide responses and reccommendations for the specific affected aspect. In your response do not forget to consider the Guidelines for Online and Blended Delivery Modes of Courses for University Institutions in Tanzania."},
                        {"role": "user", "content": input_text},
                    ],
                    max_tokens=800, 
                    temperature=0.42
                )

                response_text = response.choices[0].message.content.strip()
                break  

        cleaned_text = re.sub(r'\d+\.\s*|\*\s*', '', response_text)
        paragraphs = cleaned_text.split('\n')

        return render(request, 'gpt_response.html', {'response_text': paragraphs, 'score_interpretation': score_interpretation})

    return render(request, 'gpt_response.html')
