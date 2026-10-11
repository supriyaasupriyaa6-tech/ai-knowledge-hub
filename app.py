# ============================================================
# DSC401-6: INTERACTIVE AI Knowledge Hub — UNITS I & II
# Run: python -m streamlit run app.py
# ============================================================

import random
import time
import streamlit as st

st.set_page_config(
    page_title="AI | Units I & II",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------- DESIGN ---------------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #10152b 0%, #171b3b 55%, #24183d 100%);
    color: #f5f6ff;
}
h1, h2, h3, p, label, span, div {
    color: inherit;
}
.hero {
    padding: 35px 28px;
    border: 1px solid #414775;
    border-radius: 22px;
    background: linear-gradient(120deg, #202950, #30234d);
    text-align: center;
    margin-bottom: 24px;
}
.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}
.hero p {
    font-size: 17px;
    color: #c8ccee;
}
.panel {
    padding: 22px;
    border-radius: 18px;
    background: rgba(37, 44, 79, 0.88);
    border: 1px solid #414775;
    margin-bottom: 18px;
}
.stat {
    padding: 18px;
    border-radius: 14px;
    background: #22294a;
    border: 1px solid #414775;
    text-align: center;
}
.stat-label {
    color: #c5cbed;
    font-size: 13px;
}
.stat-value {
    color: #ffffff;
    font-size: 28px;
    font-weight: bold;
}
.question-card {
    padding: 25px;
    border-radius: 18px;
    background: #202747;
    border: 1px solid #4a5487;
    margin: 15px 0;
}
.small-muted {
    color: #c2c8e8;
    font-size: 14px;
}
div.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    min-height: 44px;
}
div[data-testid="stMetric"] {
    background: #22294a;
    border: 1px solid #414775;
    padding: 12px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------ QUESTION BANK ----------------------

QUESTIONS = [
    {
        "id": 1, "topic": "AI Foundations", "type": "MCQ",
        "difficulty": "Easy",
        "q": "Which statement best describes Artificial Intelligence?",
        "options": [
            "The study of making machines perform tasks requiring intelligence",
            "The study of computer hardware only",
            "A method used only for storing files",
            "A programming language"
        ],
        "answer": "The study of making machines perform tasks requiring intelligence",
        "why": "AI develops systems that perform tasks such as learning, reasoning, perception and decision-making.",
        "hint": "Think about machines performing tasks associated with human intelligence."
    },
    {
        "id": 2, "topic": "AI Foundations", "type": "MCQ",
        "difficulty": "Easy",
        "q": "Which of the following is a common application of AI?",
        "options": [
            "A basic chair",
            "A recommendation system suggesting movies",
            "An ordinary paper notebook",
            "A manual stapler"
        ],
        "answer": "A recommendation system suggesting movies",
        "why": "Recommendation systems use data and algorithms to suggest items that may interest a user.",
        "hint": "Choose the option that makes predictions or personalized suggestions."
    },
    {
        "id": 3, "topic": "AI Foundations", "type": "True/False",
        "difficulty": "Easy",
        "q": "Machine learning is a subfield of Artificial Intelligence.",
        "options": ["True", "False"],
        "answer": "True",
        "why": "Machine learning allows systems to learn patterns from data and is one area of AI.",
        "hint": "Machine learning is commonly used to build AI systems."
    },
    {
        "id": 4, "topic": "Turing Test", "type": "MCQ",
        "difficulty": "Easy",
        "q": "What is the main purpose of the Turing Test?",
        "options": [
            "To measure a computer's storage capacity",
            "To assess whether a machine's conversational behaviour can be distinguished from a human's",
            "To measure internet speed",
            "To test a computer's screen resolution"
        ],
        "answer": "To assess whether a machine's conversational behaviour can be distinguished from a human's",
        "why": "The test considers whether a human evaluator can distinguish a machine from a human through conversation.",
        "hint": "It concerns imitation of human conversational behaviour."
    },
    {
        "id": 5, "topic": "Turing Test", "type": "True/False",
        "difficulty": "Medium",
        "q": "Passing the Turing Test proves that a machine has consciousness.",
        "options": ["True", "False"],
        "answer": "False",
        "why": "The test evaluates observable conversational behaviour, not whether a machine is conscious.",
        "hint": "Consider whether human-like responses necessarily prove inner experience."
    },
    {
        "id": 6, "topic": "Intelligent Agents", "type": "MCQ",
        "difficulty": "Easy",
        "q": "What is a rational agent?",
        "options": [
            "An agent that always knows the future",
            "An agent that chooses actions expected to maximise its performance measure based on available information",
            "An agent that never makes a mistake",
            "An agent that performs random actions only"
        ],
        "answer": "An agent that chooses actions expected to maximise its performance measure based on available information",
        "why": "Rationality depends on the percepts, available actions, knowledge and performance measure.",
        "hint": "Rationality is about selecting an appropriate action using available information."
    },
    {
        "id": 7, "topic": "Intelligent Agents", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A vacuum-cleaning robot senses dirt and moves to clean it. What is the robot's sensor used for?",
        "options": [
            "To perform physical movement",
            "To receive information from its environment",
            "To store its final score",
            "To replace its actuators"
        ],
        "answer": "To receive information from its environment",
        "why": "Sensors collect percepts or information from the environment. Actuators carry out actions.",
        "hint": "Sensors detect; actuators act."
    },
    {
        "id": 8, "topic": "Intelligent Agents", "type": "Matching",
        "difficulty": "Medium",
        "q": "Choose the correct sensor–actuator matching for a robot.",
        "options": [
            "Camera — sensor; wheels — actuators",
            "Wheels — sensor; camera — actuator",
            "Battery — actuator; wheels — sensor",
            "Speaker — sensor; camera — actuator"
        ],
        "answer": "Camera — sensor; wheels — actuators",
        "why": "A camera receives visual information. Wheels produce movement.",
        "hint": "One component detects the surroundings; the other moves the robot."
    },
    {
        "id": 9, "topic": "Intelligent Agents", "type": "MCQ",
        "difficulty": "Medium",
        "q": "In a self-driving car, which is an example of a performance measure?",
        "options": [
            "The colour of the car",
            "Safe arrival while obeying traffic rules and using reasonable time",
            "The brand of the camera",
            "The number of buttons on the dashboard"
        ],
        "answer": "Safe arrival while obeying traffic rules and using reasonable time",
        "why": "A performance measure specifies the criteria used to evaluate an agent's behaviour.",
        "hint": "Choose a criterion describing how well the car performs its task."
    },
    {
        "id": 10, "topic": "Intelligent Agents", "type": "MCQ",
        "difficulty": "Easy",
        "q": "Which sequence correctly represents the basic agent interaction cycle?",
        "options": [
            "Actuators → percepts → sensors",
            "Sensors receive percepts → agent selects an action → actuators carry it out",
            "Action → delete environment → sensor",
            "Database → printer → keyboard"
        ],
        "answer": "Sensors receive percepts → agent selects an action → actuators carry it out",
        "why": "An agent perceives the environment through sensors and affects it through actuators.",
        "hint": "Perceive first, decide next, act after that."
    },
    {
        "id": 11, "topic": "Task Environments", "type": "MCQ",
        "difficulty": "Medium",
        "q": "A chess-playing agent can observe the entire board. In terms of observability, chess is usually treated as:",
        "options": [
            "Fully observable",
            "Partially observable",
            "Unobservable",
            "Randomly observable"
        ],
        "answer": "Fully observable",
        "why": "The board position and legal pieces are visible to both players, although the opponent's future choices are unknown.",
        "hint": "Ask whether the current state of the board can be observed."
    },
    {
        "id": 12, "topic": "Task Environments", "type": "MCQ",
        "difficulty": "Medium",
        "q": "Why is driving in real-world traffic considered dynamic?",
        "options": [
            "Nothing changes while the agent decides",
            "Other vehicles and road conditions can change over time",
            "The road always has one fixed state",
            "The car cannot receive new information"
        ],
        "answer": "Other vehicles and road conditions can change over time",
        "why": "A dynamic environment may change while the agent is deciding or acting.",
        "hint": "Think about what other road users do while the car is planning."
    },
    {
        "id": 13, "topic": "Task Environments", "type": "True/False",
        "difficulty": "Medium",
        "q": "A deterministic environment is one in which the current state and action uniquely determine the next state.",
        "options": ["True", "False"],
        "answer": "True",
        "why": "In a deterministic environment, the outcome of an action is determined by the current state and action.",
        "hint": "Deterministic means the outcome is determined rather than uncertain."
    },
    {
        "id": 14, "topic": "Problem Solving", "type": "MCQ",
        "difficulty": "Easy",
        "q": "What is a state space in a search problem?",
        "options": [
            "The set of possible states reachable or considered in the problem",
            "Only the final answer",
            "The physical memory of a computer",
            "A list of programming languages"
        ],
        "answer": "The set of possible states reachable or considered in the problem",
        "why": "A state space represents possible configurations of a problem and the transitions between them.",
        "hint": "It includes the different configurations the search may consider."
    },
    {
        "id": 15, "topic": "Problem Solving", "type": "MCQ",
        "difficulty": "Medium",
        "q": "Which elements are normally included when formulating a search problem?",
        "options": [
            "Initial state, actions, transition model, goal test and path cost",
            "Only a title and a picture",
            "Only the programming language",
            "Only the goal state"
        ],
        "answer": "Initial state, actions, transition model, goal test and path cost",
        "why": "These elements define where the search starts, how states change, how success is recognised and how paths are evaluated.",
        "hint": "A search problem needs a start, possible actions, a goal test and a way to evaluate paths."
    },
    {
        "id": 16, "topic": "Problem Solving", "type": "MCQ",
        "difficulty": "Medium",
        "q": "In a production system, what is a production rule commonly represented as?",
        "options": [
            "IF condition THEN action",
            "Only a graph title",
            "A random number without a condition",
            "A computer's physical address"
        ],
        "answer": "IF condition THEN action",
        "why": "Production systems commonly use condition–action rules to determine which action to apply.",
        "hint": "The rule checks a condition and specifies what to do."
    },
    {
        "id": 17, "topic": "Problem Solving", "type": "Scenario",
        "difficulty": "Medium",
        "q": "Two routes reach the same destination. One has 4 steps costing 2 each; another has 3 steps costing 5 each. Which route has the lower path cost?",
        "options": [
            "The 4-step route, with cost 8",
            "The 3-step route, with cost 15",
            "Both routes have cost 10",
            "The costs cannot be calculated"
        ],
        "answer": "The 4-step route, with cost 8",
        "why": "The first route costs 4 × 2 = 8. The second costs 3 × 5 = 15. Fewer steps do not always mean lower cost.",
        "hint": "Multiply the number of steps by the cost per step for each route."
    },
    {
        "id": 18, "topic": "Search Algorithms", "type": "MCQ",
        "difficulty": "Medium",
        "q": "Why is the order of node expansion important in search algorithms?",
        "options": [
            "It can affect which solution is found and the resources used",
            "It changes the meaning of the goal test",
            "It always removes the need for memory",
            "It guarantees that every algorithm returns the same path"
        ],
        "answer": "It can affect which solution is found and the resources used",
        "why": "Different search strategies explore nodes in different orders, affecting efficiency and solution properties.",
        "hint": "Consider the number of nodes explored and the path discovered."
    },
    {
        "id": 19, "topic": "Search Algorithms", "type": "Problem Solving",
        "difficulty": "Medium",
        "q": "A tree has root A, children B and C, and B has children D and E. Using left-to-right Breadth-First Search, what is the visit order until E?",
        "options": [
            "A, B, C, D, E",
            "A, B, D, E, C",
            "A, C, B, E, D",
            "D, E, B, C, A"
        ],
        "answer": "A, B, C, D, E",
        "why": "BFS visits nodes level by level, using a queue. It visits A, then B and C, then D and E.",
        "hint": "Finish the current level before moving to the next level."
    },
    {
        "id": 20, "topic": "Search Algorithms", "type": "MCQ",
        "difficulty": "Medium",
        "q": "Under the usual assumptions of finite branching, Breadth-First Search is:",
        "options": [
            "Complete and optimal when all step costs are equal",
            "Always incomplete",
            "Always optimal regardless of step costs",
            "Unable to find a goal state"
        ],
        "answer": "Complete and optimal when all step costs are equal",
        "why": "BFS finds the shallowest goal and is optimal when each step has the same cost.",
        "hint": "BFS minimises the number of steps, which minimises cost only when step costs are equal."
    },
    {
        "id": 21, "topic": "Search Algorithms", "type": "Problem Solving",
        "difficulty": "Medium",
        "q": "A tree has root A, left child B and right child C. B has children D and E. With left-first Depth-First Search, which nodes are visited first?",
        "options": [
            "A, B, D",
            "A, B, C",
            "A, C, B",
            "D, E, B"
        ],
        "answer": "A, B, D",
        "why": "DFS explores a branch deeply before returning to explore siblings.",
        "hint": "Follow the left branch as far as possible first."
    },
    {
        "id": 22, "topic": "Search Algorithms", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A DFS search follows an infinite branch that never reaches a goal. What is a potential problem?",
        "options": [
            "It may never return to explore another branch",
            "It must immediately find the shallowest goal",
            "It always uses a queue",
            "It automatically becomes BFS"
        ],
        "answer": "It may never return to explore another branch",
        "why": "In an infinite-depth search space, ordinary DFS can get trapped following one branch indefinitely.",
        "hint": "DFS prioritises depth and may not return from an infinite branch."
    },
    {
        "id": 23, "topic": "Search Algorithms", "type": "MCQ",
        "difficulty": "Medium",
        "q": "How does Iterative Deepening Search operate?",
        "options": [
            "It repeatedly performs depth-limited search with increasing limits",
            "It always explores only the rightmost node",
            "It uses only heuristic values",
            "It never revisits the root"
        ],
        "answer": "It repeatedly performs depth-limited search with increasing limits",
        "why": "The depth limit is increased in successive iterations until a goal is found.",
        "hint": "Imagine searching to depth 0, then depth 1, then depth 2, and so on."
    },
    {
        "id": 24, "topic": "Search Algorithms", "type": "Problem Solving",
        "difficulty": "Medium",
        "q": "A goal is at depth 2 and another goal is at depth 4. In a tree with equal step costs, which goal will BFS find first if both are reachable?",
        "options": [
            "The goal at depth 2",
            "The goal at depth 4",
            "Always the rightmost goal",
            "It cannot find either goal"
        ],
        "answer": "The goal at depth 2",
        "why": "BFS expands shallower levels before deeper levels.",
        "hint": "BFS explores in increasing order of depth."
    },
    {
        "id": 25, "topic": "Search Algorithms", "type": "Problem Solving",
        "difficulty": "Medium",
        "q": "A path has three edges with costs 4, 2 and 7. What is its total path cost?",
        "options": ["9", "11", "13", "28"],
        "answer": "13",
        "why": "The total path cost is 4 + 2 + 7 = 13.",
        "hint": "Add the costs of all edges on the path."
    },
    {
        "id": 26, "topic": "Hill Climbing", "type": "MCQ",
        "difficulty": "Medium",
        "q": "What is a local optimum in hill climbing?",
        "options": [
            "A state better than its neighbours but not necessarily the best overall",
            "Always the globally best state",
            "The initial state in every problem",
            "A state that has no value"
        ],
        "answer": "A state better than its neighbours but not necessarily the best overall",
        "why": "Hill climbing may stop at a state that is locally best while a better state exists elsewhere.",
        "hint": "Local means compared with nearby states, not every state in the search space."
    },
    {
        "id": 27, "topic": "Hill Climbing", "type": "MCQ",
        "difficulty": "Medium",
        "q": "What is a common feature of stochastic hill climbing?",
        "options": [
            "It randomly selects among suitable uphill moves",
            "It always explores every state in breadth-first order",
            "It never uses an evaluation function",
            "It always chooses the first node in a queue"
        ],
        "answer": "It randomly selects among suitable uphill moves",
        "why": "Stochastic hill climbing chooses a candidate improving move using a randomised selection strategy.",
        "hint": "Focus on the word stochastic, which indicates randomness."
    },
    {
        "id": 28, "topic": "Hill Climbing", "type": "MCQ",
        "difficulty": "Medium",
        "q": "How can random-restart hill climbing help with local optima?",
        "options": [
            "It starts hill climbing from multiple initial states",
            "It permanently removes the goal test",
            "It guarantees that every state is visited",
            "It converts every problem into BFS"
        ],
        "answer": "It starts hill climbing from multiple initial states",
        "why": "Different starting states may lead to different regions of the search space, improving the chance of finding a better solution.",
        "hint": "The method repeats the search from different starting points."
    },
    {
        "id": 29, "topic": "Heuristic Search", "type": "MCQ",
        "difficulty": "Easy",
        "q": "What does a heuristic function h(n) estimate in many search problems?",
        "options": [
            "The estimated cost from node n to a goal",
            "The number of letters in a node's name",
            "The computer's battery percentage",
            "The actual cost of every possible path with certainty"
        ],
        "answer": "The estimated cost from node n to a goal",
        "why": "A heuristic provides an estimate of how far or costly it may be to reach a goal.",
        "hint": "It helps guide the search toward a goal."
    },
    {
        "id": 30, "topic": "Heuristic Search", "type": "MCQ",
        "difficulty": "Medium",
        "q": "Which evaluation does Greedy Best-First Search commonly use to choose a node?",
        "options": [
            "f(n) = h(n)",
            "f(n) = g(n) + h(n)",
            "f(n) = g(n) × h(n)",
            "f(n) = 0 for every node"
        ],
        "answer": "f(n) = h(n)",
        "why": "Greedy Best-First Search prioritises the estimated remaining cost h(n), without adding the path cost g(n).",
        "hint": "Greedy Best-First focuses on the estimated distance to the goal."
    },
    {
        "id": 31, "topic": "Heuristic Search", "type": "Problem Solving",
        "difficulty": "Medium",
        "q": "Greedy Best-First Search has frontier nodes P, Q and R with h(P)=8, h(Q)=3 and h(R)=5. Which node is selected next?",
        "options": ["P", "Q", "R", "All three simultaneously"],
        "answer": "Q",
        "why": "Greedy Best-First Search selects the node with the smallest heuristic value, which is Q with h=3.",
        "hint": "Select the smallest h-value."
    },
    {
        "id": 32, "topic": "Heuristic Search", "type": "MCQ",
        "difficulty": "Medium",
        "q": "Why is Greedy Best-First Search not generally guaranteed to find the lowest-cost path?",
        "options": [
            "It prioritises estimated remaining cost and may ignore the path cost already incurred",
            "It always expands nodes in increasing path-cost order",
            "It never uses a heuristic",
            "It can only search a single node"
        ],
        "answer": "It prioritises estimated remaining cost and may ignore the path cost already incurred",
        "why": "Greedy Best-First uses h(n), while algorithms such as A* use g(n)+h(n).",
        "hint": "It considers the estimate to the goal, not the cost already spent."
    },
    {
        "id": 33, "topic": "Constraint Satisfaction Problems", "type": "MCQ",
        "difficulty": "Easy",
        "q": "In a Constraint Satisfaction Problem (CSP), what is a domain?",
        "options": [
            "The set of possible values that a variable can take",
            "The final score of the quiz",
            "The order in which a website loads",
            "The number of computer users"
        ],
        "answer": "The set of possible values that a variable can take",
        "why": "A CSP consists of variables, their domains and constraints restricting allowed combinations of values.",
        "hint": "A domain lists the possible values for a variable."
    },
    {
        "id": 34, "topic": "Constraint Satisfaction Problems", "type": "MCQ",
        "difficulty": "Easy",
        "q": "What is the purpose of a constraint in a CSP?",
        "options": [
            "To specify which combinations of variable values are allowed",
            "To make every variable take every value",
            "To delete all variables",
            "To display the final score"
        ],
        "answer": "To specify which combinations of variable values are allowed",
        "why": "Constraints restrict assignments so that only valid combinations satisfy the problem.",
        "hint": "A constraint tells you what is allowed or forbidden."
    },
    {
        "id": 35, "topic": "Constraint Satisfaction Problems", "type": "MCQ",
        "difficulty": "Medium",
        "q": "How does backtracking solve a CSP?",
        "options": [
            "It assigns variables and reverses assignments when a conflict occurs",
            "It ignores all constraints",
            "It assigns only one value and stops",
            "It always uses hill climbing"
        ],
        "answer": "It assigns variables and reverses assignments when a conflict occurs",
        "why": "Backtracking explores assignments systematically and returns to an earlier variable when an assignment violates constraints.",
        "hint": "If an assignment leads to a conflict, undo it and try another value."
    },
    {
        "id": 36, "topic": "Constraint Satisfaction Problems", "type": "Matching",
        "difficulty": "Medium",
        "q": "Which matching correctly identifies the three main parts of a CSP?",
        "options": [
            "Variables = what to assign; domains = possible values; constraints = restrictions",
            "Variables = restrictions; domains = final scores; constraints = possible values",
            "Variables = actions; domains = sensors; constraints = actuators",
            "Variables = answers; domains = web pages; constraints = colours only"
        ],
        "answer": "Variables = what to assign; domains = possible values; constraints = restrictions",
        "why": "Variables are the unknowns, domains list their possible values and constraints define valid assignments.",
        "hint": "Think unknowns, choices and rules."
    },
    {
        "id": 37, "topic": "Constraint Satisfaction Problems", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A college timetable must assign exams to time slots. Two exams taken by the same student cannot be at the same time. What is this an example of?",
        "options": [
            "A Constraint Satisfaction Problem",
            "A Turing Test",
            "A sensor actuator cycle only",
            "A database backup"
        ],
        "answer": "A Constraint Satisfaction Problem",
        "why": "Exam assignments are variables, time slots are domains and the no-overlap rule is a constraint.",
        "hint": "The task assigns values while obeying restrictions."
    },
    {
        "id": 38, "topic": "Problem Solving", "type": "MCQ",
        "difficulty": "Medium",
        "q": "What is means–ends analysis?",
        "options": [
            "Comparing the current state with the goal and selecting actions that reduce the difference",
            "Choosing actions without considering the goal",
            "Sorting data alphabetically",
            "Exploring every node randomly"
        ],
        "answer": "Comparing the current state with the goal and selecting actions that reduce the difference",
        "why": "Means–ends analysis identifies differences between the current and goal states and chooses operators to reduce them.",
        "hint": "Compare where you are with where you want to be."
    },
    {
        "id": 39, "topic": "Problem Solving", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A student wants to upload an assignment but has not completed it. The student first completes the work, then saves the file, then uploads it. Which approach does this resemble?",
        "options": [
            "Means–ends analysis",
            "Random guessing",
            "A Turing Test",
            "Blindly selecting a node without a goal"
        ],
        "answer": "Means–ends analysis",
        "why": "The student identifies what separates the current state from the goal and takes actions to reduce that difference.",
        "hint": "The steps are chosen to reduce the gap between the current state and the desired result."
    },
    {
        "id": 40, "topic": "AI Applications", "type": "Scenario",
        "difficulty": "Easy",
        "q": "A streaming platform recommends movies based on viewing history. Which AI application is this?",
        "options": [
            "Recommendation system",
            "Industrial welding only",
            "Manual file storage",
            "A mechanical clock"
        ],
        "answer": "Recommendation system",
        "why": "Recommendation systems analyse user preferences and behaviour to suggest relevant content.",
        "hint": "The platform suggests what a user might like."
    },
    {
        "id": 41, "topic": "AI Applications", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A bank's model flags an unusual transaction as potentially fraudulent. Which task is being performed?",
        "options": [
            "Anomaly detection",
            "Image compression only",
            "Manual sorting",
            "Speech synthesis"
        ],
        "answer": "Anomaly detection",
        "why": "Anomaly detection identifies patterns that differ from expected behaviour and may warrant investigation.",
        "hint": "The system looks for unusual patterns."
    },
    {
        "id": 42, "topic": "AI Applications", "type": "MCQ",
        "difficulty": "Easy",
        "q": "Which AI area is most directly used to convert spoken words into written text?",
        "options": [
            "Speech recognition",
            "Constraint satisfaction only",
            "Image resizing",
            "Spreadsheet formatting"
        ],
        "answer": "Speech recognition",
        "why": "Speech recognition systems process audio and identify the words being spoken.",
        "hint": "The input is spoken language."
    },
    {
        "id": 43, "topic": "AI Applications", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A warehouse robot detects shelves, plans a route and moves a package. Which combination best describes its tasks?",
        "options": [
            "Perception, planning and action",
            "Only text formatting",
            "Only data storage",
            "Only speech generation"
        ],
        "answer": "Perception, planning and action",
        "why": "The robot perceives its surroundings, plans how to reach its destination and acts using its movement system.",
        "hint": "It must understand its surroundings, decide on a route and move."
    },
    {
        "id": 44, "topic": "AI Applications", "type": "MCQ",
        "difficulty": "Easy",
        "q": "Which AI field is central to understanding and generating human language in chatbots?",
        "options": [
            "Natural Language Processing",
            "Mechanical engineering only",
            "File compression",
            "Network cabling"
        ],
        "answer": "Natural Language Processing",
        "why": "Natural Language Processing (NLP) deals with computational processing of human language.",
        "hint": "The field's name includes the word language."
    },
    {
        "id": 45, "topic": "AI Applications", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A farmer uses a phone camera and an AI model to identify disease symptoms on crop leaves. Which technique is most directly involved?",
        "options": [
            "Computer vision and image classification",
            "Only path-cost calculation",
            "Only database indexing",
            "A Turing Test"
        ],
        "answer": "Computer vision and image classification",
        "why": "Computer vision processes images, and image classification can assign a disease or health category to a leaf image.",
        "hint": "The input is an image captured by a camera."
    },
    {
        "id": 46, "topic": "AI Applications", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A navigation system changes its recommended route when traffic conditions change. What property of the environment is important here?",
        "options": [
            "Dynamic",
            "Static",
            "Fully predictable in every situation",
            "Without states"
        ],
        "answer": "Dynamic",
        "why": "Traffic conditions change over time, so a navigation agent may need to update its decisions.",
        "hint": "Road conditions do not remain fixed."
    },
    {
        "id": 47, "topic": "AI Applications", "type": "Scenario",
        "difficulty": "Medium",
        "q": "An irrigation system checks soil moisture and waters crops when the soil is too dry. What kind of AI system does this resemble?",
        "options": [
            "An intelligent agent that senses and acts",
            "A system without inputs or outputs",
            "A Turing Test evaluator",
            "A search tree with no actions"
        ],
        "answer": "An intelligent agent that senses and acts",
        "why": "It receives information from a sensor and selects an action based on the observed conditions.",
        "hint": "It measures a condition and takes an action in response."
    },
    {
        "id": 48, "topic": "AI Applications", "type": "Scenario",
        "difficulty": "Medium",
        "q": "A factory uses AI to inspect product images for defects. Why should the system be evaluated on examples it did not train on?",
        "options": [
            "To assess how well it generalises to unseen examples",
            "To ensure it memorises only the training images",
            "To remove the need for evaluation",
            "To guarantee every image is identical"
        ],
        "answer": "To assess how well it generalises to unseen examples",
        "why": "Testing on unseen examples helps estimate how well a model performs beyond its training data.",
        "hint": "The aim is to see whether the model works on new examples."
    },
    {
        "id": 49, "topic": "Search Algorithms", "type": "Assertion–Reason",
        "difficulty": "Hard",
        "q": "Assertion (A): Breadth-First Search expands the shallowest unexpanded nodes first. Reason (R): BFS typically uses a FIFO queue.",
        "options": [
            "Both A and R are true, and R correctly explains A",
            "Both A and R are true, but R does not explain A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "answer": "Both A and R are true, and R correctly explains A",
        "why": "A FIFO queue expands nodes in the order they are discovered, resulting in level-by-level exploration.",
        "hint": "FIFO means first in, first out."
    },
    {
        "id": 50, "topic": "Intelligent Agents", "type": "Assertion–Reason",
        "difficulty": "Hard",
        "q": "Assertion (A): A rational agent must always achieve the best possible outcome. Reason (R): Rationality is judged using the information available to the agent and its performance measure.",
        "options": [
            "Both A and R are true, and R correctly explains A",
            "Both A and R are true, but R does not explain A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "answer": "A is false, but R is true",
        "why": "A rational agent selects an action expected to perform well given its information. It cannot guarantee the best possible outcome in every uncertain environment.",
        "hint": "Rational behaviour does not mean perfect knowledge or guaranteed success."
    }
]

# Divide all 50 questions into fixed levels:
# Easy = 17 questions; Medium = 17 questions; Hard = 16 questions.
# The questions and their answers remain unchanged.
for question in QUESTIONS:
    if question["id"] <= 17:
        question["difficulty"] = "Easy"
    elif question["id"] <= 34:
        question["difficulty"] = "Medium"
    else:
        question["difficulty"] = "Hard"

# ------------------------- STATE SETUP ------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

if "used_hints" not in st.session_state:
    st.session_state.used_hints = set()


def start_quiz(name, difficulty):
    available = QUESTIONS.copy()

    if difficulty != "All":
        available = [
            q for q in available
            if q["difficulty"] == difficulty
        ]

    random.shuffle(available)

    st.session_state.player_name = name.strip() or "Player"
    st.session_state.selected_questions = available
    st.session_state.question_count = len(available)

    # Fixed timer: 30 seconds per question
    st.session_state.timer_seconds = 30

    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.answers = []
    st.session_state.streak = 0
    st.session_state.best_streak = 0
    st.session_state.feedback = None
    st.session_state.answered = False
    st.session_state.hint_used = False
    st.session_state.timed_out = False
    st.session_state.question_started_at = time.time()
    st.session_state.used_hints = set()
    st.session_state.page = "quiz"


def finish_quiz():
    if st.session_state.page == "quiz":
        score = st.session_state.score
        total = len(st.session_state.selected_questions)
        accuracy = round((score / total) * 100, 1) if total else 0

        st.session_state.leaderboard.append({
            "Player": st.session_state.player_name,
            "Score": f"{score}/{total}",
            "Accuracy": f"{accuracy}%",
            "Best streak": st.session_state.best_streak
        })

        st.session_state.leaderboard.sort(
            key=lambda x: (
                int(x["Score"].split("/")[0]),
                x["Best streak"]
            ),
            reverse=True
        )

        st.session_state.leaderboard = st.session_state.leaderboard[:10]

    st.session_state.page = "results"


def record_answer(selected_answer, timed_out=False):
    if st.session_state.answered:
        return

    question = st.session_state.selected_questions[
        st.session_state.current
    ]

    correct = selected_answer == question["answer"]

    if correct:
        st.session_state.score += 1
        st.session_state.streak += 1
        st.session_state.best_streak = max(
            st.session_state.best_streak,
            st.session_state.streak
        )
        message = "Correct! 🎉"
    else:
        st.session_state.lives -= 1
        st.session_state.streak = 0
        message = "Time's up!" if timed_out else "Not quite!"

    st.session_state.answers.append({
        "id": question["id"],
        "question": question["q"],
        "selected": selected_answer if selected_answer else "No answer",
        "correct_answer": question["answer"],
        "correct": correct,
        "explanation": question["why"],
        "topic": question["topic"]
    })

    st.session_state.feedback = {
        "correct": correct,
        "message": message,
        "explanation": question["why"],
        "correct_answer": question["answer"],
        "timed_out": timed_out
    }

    st.session_state.answered = True
    st.session_state.timed_out = False


def next_question():
    if st.session_state.lives <= 0:
        finish_quiz()
    elif st.session_state.current + 1 >= len(
        st.session_state.selected_questions
    ):
        finish_quiz()
    else:
        st.session_state.current += 1
        st.session_state.feedback = None
        st.session_state.answered = False
        st.session_state.hint_used = False
        st.session_state.timed_out = False
        st.session_state.question_started_at = time.time()


# ----------------------- TIMER COMPONENT ----------------------

@st.fragment(run_every="1s")
def timer_display():
    if st.session_state.page != "quiz":
        return

    if st.session_state.answered:
        return

    elapsed = time.time() - st.session_state.question_started_at
    remaining = max(
        0,
        int(st.session_state.timer_seconds - elapsed)
    )

    st.markdown(
        f"<div class='stat'>"
        f"<div class='stat-label'>TIME REMAINING</div>"
        f"<div class='stat-value'>⏱️ {remaining}s</div>"
        f"</div>",
        unsafe_allow_html=True
    )

    if remaining <= 0 and not st.session_state.answered:
        record_answer(None, timed_out=True)
        st.rerun(scope="app")


# ------------------------- HOME PAGE --------------------------

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <h1>AI Knowledge Hub</h1>
        <p>Test Your Artificial Intelligence Knowledge</p>
        <p>Think smart. Solve problems. Explore AI.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="stat">
            <div class="stat-label">QUESTION BANK</div>
            <div class="stat-value">50</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat">
            <div class="stat-label">LIVES PER GAME</div>
            <div class="stat-value">❤️ 3</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat">
            <div class="stat-label">TIME PER QUESTION</div>
            <div class="stat-value">⏱️ 30s</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Ready to play?")
    st.write(
        "Choose your difficulty level. The game will automatically "
        "load all questions assigned to that level."
    )

    with st.form("start_quiz_form"):
        player_name = st.text_input(
            "Player name",
            value="Player",
            max_chars=25
        )

        difficulty = st.selectbox(
            "Choose difficulty level",
            ["All", "Easy", "Medium", "Hard"]
        )

        start_button = st.form_submit_button(
            "🚀 Start Quiz",
            use_container_width=True
        )

        if start_button:
            start_quiz(player_name, difficulty)
            st.rerun()

    with st.expander("📚 Topics covered"):
        st.markdown("""
        - Foundations and applications of Artificial Intelligence
        - Turing Test
        - Intelligent and rational agents
        - Sensors, actuators and performance measures
        - Task environments
        - Problem formulation and state spaces
        - Production systems and means–ends analysis
        - Breadth-First Search and Depth-First Search
        - Iterative Deepening Search
        - Hill climbing and its variations
        - Heuristic and Greedy Best-First Search
        - Constraint Satisfaction Problems
        - Real-world AI applications
        """)

    with st.expander("🎮 How to play"):
        st.markdown("""
        1. Enter your player name and choose a difficulty level.
        2. Each question has a fixed 30-second timer.
        3. Use the hint button if you need help.
        4. You begin with three lives. An incorrect or unanswered
           question costs one life.
        5. Your score, accuracy, best streak and answer review
           appear on the results screen.
        """)


# ------------------------- QUIZ PAGE --------------------------

elif st.session_state.page == "quiz":

    total = len(st.session_state.selected_questions)
    current_index = st.session_state.current
    question = st.session_state.selected_questions[current_index]

    if current_index >= total:
        finish_quiz()
        st.rerun()

    st.markdown("""
    <div class="hero">
        <h1>AI Knowledge Hub</h1>
        <p>Stay focused. Every question counts.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Question", f"{current_index + 1}/{total}")

    with col2:
        st.metric("Score", st.session_state.score)

    with col3:
        st.metric("Lives", "❤️ " * st.session_state.lives)

    with col4:
        st.metric("Best streak", st.session_state.best_streak)

    st.progress((current_index + 1) / total)

    left, right = st.columns([3, 1])

    with left:
        st.markdown(
            f"<div class='small-muted'>"
            f"TOPIC: {question['topic']} &nbsp; | &nbsp; "
            f"TYPE: {question['type']} &nbsp; | &nbsp; "
            f"DIFFICULTY: {question['difficulty']}"
            f"</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='question-card'>"
            f"<h3>Question {current_index + 1}</h3>"
            f"<p style='font-size:20px'>{question['q']}</p>"
            f"</div>",
            unsafe_allow_html=True
        )

    with right:
        timer_display()

    if not st.session_state.answered:

        if st.button(
            "💡 Show Hint",
            use_container_width=True,
            disabled=st.session_state.hint_used
        ):
            st.session_state.hint_used = True
            st.session_state.used_hints.add(question["id"])

        if st.session_state.hint_used:
            st.info("Hint: " + question["hint"])

        with st.form(f"answer_form_{question['id']}"):
            selected_answer = st.radio(
                "Choose your answer:",
                question["options"],
                index=None,
                key=f"answer_{question['id']}"
            )

            submitted = st.form_submit_button(
                "Submit Answer",
                use_container_width=True
            )

            if submitted:
                if selected_answer is None:
                    st.warning("Please select an answer first.")
                else:
                    record_answer(selected_answer)
                    st.rerun()

    else:
        feedback = st.session_state.feedback

        if feedback["correct"]:
            st.success(feedback["message"])
        else:
            st.error(feedback["message"])
            st.write(
                "**Correct answer:** "
                + feedback["correct_answer"]
            )

        st.info("**Explanation:** " + feedback["explanation"])

        if st.session_state.lives <= 0:
            st.warning("You have used all three lives. Quiz over!")

        button_label = (
            "🏁 View Results"
            if (
                st.session_state.lives <= 0
                or current_index + 1 >= total
            )
            else "➡️ Next Question"
        )

        if st.button(button_label, use_container_width=True):
            next_question()
            st.rerun()

    with st.expander("📊 Quiz progress"):
        st.write(f"Questions completed: {len(st.session_state.answers)}")
        st.write(f"Correct answers: {st.session_state.score}")
        st.write(
            "Incorrect answers: "
            f"{len(st.session_state.answers) - st.session_state.score}"
        )
        st.write(f"Best streak: {st.session_state.best_streak}")


# ------------------------ RESULTS PAGE ------------------------

elif st.session_state.page == "results":

    answers = st.session_state.answers
    total_questions = len(st.session_state.selected_questions)
    score = st.session_state.score
    accuracy = round((score / total_questions) * 100, 1) if total_questions else 0

    st.markdown("""
    <div class="hero">
        <h1>🏆 Quiz Complete!</h1>
        <p>Great effort! Here's how you performed.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### Well played, {st.session_state.player_name}!")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Final Score", f"{score}/{total_questions}")

    with col2:
        st.metric("Accuracy", f"{accuracy}%")

    with col3:
        st.metric(
            "Correct",
            sum(1 for a in answers if a["correct"])
        )

    with col4:
        st.metric(
            "Best Streak",
            st.session_state.best_streak
        )

    incorrect_count = sum(1 for a in answers if not a["correct"])

    st.markdown("### 📈 Performance summary")
    st.write(f"- Correct answers: **{score}**")
    st.write(f"- Incorrect or timed-out answers: **{incorrect_count}**")
    st.write(f"- Hints used: **{len(st.session_state.used_hints)}**")
    st.progress(accuracy / 100)

    if accuracy >= 80:
        st.success("Excellent work! You have a strong understanding of these topics.")
    elif accuracy >= 60:
        st.info("Good effort! Review the questions you missed to improve further.")
    else:
        st.warning("Keep practising! Read the explanations and try another round.")

    st.markdown("## 📝 Answer Review")

    if not answers:
        st.info("No answers were submitted in this session.")
    else:
        for number, item in enumerate(answers, start=1):
            label = "✅ Correct" if item["correct"] else "❌ Incorrect"

            with st.expander(f"{number}. {label} — {item['topic']}"):
                st.write("**Question:**", item["question"])
                st.write("**Your answer:**", item["selected"])
                st.write("**Correct answer:**", item["correct_answer"])
                st.write("**Explanation:**", item["explanation"])

    st.markdown("## 🏅 Session Leaderboard")

    if st.session_state.leaderboard:
        st.dataframe(
            st.session_state.leaderboard,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.write("Your session leaderboard will appear here.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Play Again", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        if st.button("📚 Review Question Bank", use_container_width=True):
            st.session_state.page = "bank"
            st.rerun()


# ------------------------ QUESTION BANK -----------------------

elif st.session_state.page == "bank":

    st.markdown("""
    <div class="hero">
        <h1>📚 AI Question Bank</h1>
        <p>Review questions, correct answers and explanations.</p>
    </div>
    """, unsafe_allow_html=True)

    topics = sorted(set(q["topic"] for q in QUESTIONS))
    selected_topic = st.selectbox(
        "Filter by topic",
        ["All Topics"] + topics
    )
    search_text = st.text_input("Search questions")

    filtered = QUESTIONS

    if selected_topic != "All Topics":
        filtered = [
            q for q in filtered
            if q["topic"] == selected_topic
        ]

    if search_text.strip():
        filtered = [
            q for q in filtered
            if search_text.lower() in q["q"].lower()
            or search_text.lower() in q["topic"].lower()
        ]

    st.write(f"Showing **{len(filtered)}** questions.")

    for question in filtered:
        with st.expander(f"Q{question['id']}. {question['q']}"):
            st.write(f"**Topic:** {question['topic']}")
            st.write(f"**Type:** {question['type']}")
            st.write(f"**Difficulty:** {question['difficulty']}")

            for option in question["options"]:
                st.write("- " + option)

            st.success("Correct answer: " + question["answer"])
            st.write("**Explanation:** " + question["why"])
            st.write("**Hint:** " + question["hint"])

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()