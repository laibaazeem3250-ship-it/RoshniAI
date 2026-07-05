# RoshniAI Agent Skills
## Agent: Student Profile Agent
skill: collect_student_profile
description: Collects student information for university matching
triggers: [grades, marks, budget, country, field, study]
steps:
  1. Ask for student grades/percentage
  2. Ask for annual budget in USD
  3. Ask for preferred country
  4. Ask for field of study
  5. Output STUDENT PROFILE COMPLETE when all collected
 
## Agent: University Finder Agent  
skill: search_universities
description: Finds best matching universities worldwide 
triggers: [university, college, admission, degree, campus]
knowledge_base:
  - Pakistan: LUMS, NUST, UET, COMSATS, IBA
  - USA: MIT, Stanford, Harvard, Carnegie Mellon
  - Turkey: Bogazici, METU, Bilkent, Sabanci, Koc
  - Malaysia: UM, UTM, UPM, Taylor's, Monash
  - UK: Oxford, Cambridge, Imperial, UCL
  - China: Tsinghua, Peking University, Fudan
  - Korea: Seoul National, KAIST, Yonsei
  - Singapore: NUS, NTU
  - Germany: TU Munich, Heidelberg
  - Australia: Melbourne, ANU, Sydney
steps:
  1. Read STUDENT PROFILE COMPLETE
  2. Match grades to university requirements
  3. Filter by budget and country preference
  4. Rank by world ranking
  5. Return top 5 with fees and deadlines

## Agent: Scholarship Hunter Agent
skill: find_scholarships
description: Finds fully funded and partial scholarships
triggers: [scholarship, funding, financial aid, grant, stipend]
types:
  - Fully funded (tuition + living + flights)
  - Partial (tuition only)
  - Merit based (grades focused)
  - Need based (budget focused)
steps:
  1. Read student profile and country preference
  2. Search country specific scholarships
  3. Match eligibility requirements
  4. Return top 5 with deadlines and coverage

## Security Evaluation (Day 4)
skill: evaluate_safety
description: Validates all inputs and outputs for safety
checks:
  - Input length validation
  - Harmful content detection  
  - Output quality scoring
  - Human in the loop for sensitive advice

## Memory System (Day 2)
skill: remember_student
description: Saves and loads student profiles across sessions
storage: memory.json
operations:
  - save: Store profile after completion
  - load: Retrieve previous session data
  