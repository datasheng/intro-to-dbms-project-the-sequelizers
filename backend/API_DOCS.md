# API Docs

### Endpoint: `/get_courses`

### Parameters

- `q` (optional): A search query to filter courses by their subject, level, or name. This performs a partial match.
- `id` (optional): The course ID to filter the courses. This performs an exact match.

### Example Requests and Response

#### 1. Retrieve all courses

```http
GET /get_courses
```
#### Response
```json
[
  {
    "course_id": 1,
    "course_level": 10300,
    "credits": 3,
    "description": "Intensive introduction to computing, tailored to the needs of those majoring in computer science and computer engineering. Introduction to programming in a modern object-oriented programming language such as C++, with particular emphasis on the logical evolution of working programs from specifications.",
    "name": "Introduction to Computing for Majors",
    "subject": "CSC"
  },
  {
    "course_id": 2,
    "course_level": 10400,
    "credits": 4,
    "description": "Introduction to the mathematics fundamental to all phases of computer science, from the formulation of problems to the understanding of their underlying structure, to the comparative analysis of the complexity of algorithms that can be used to solve these problems. The course introduces combinatorics, first-order logic, induction, set theory, relations and functions, graphs, trees, and number theory.",
    "name": "Discrete Mathematical Structures",
    "subject": "CSC"
  },
  {
    "course_id": 3,
    "course_level": 11300,
    "credits": 1,
    "description": "This course designed to develop understanding of and fluency in current and important programming languages.  Specifically, this class will teach the fluency in Python.  The course is intended for those who have already learned object-oriented concepts in at least one programming language.  A series of programming projects is an essential component of the course.",
    "name": "Programming Language",
    "subject": "CSC"
  },
  ...
]
```

#### 2. Retrieve a course by ID
```http
GET /get_courses?id=1
```
#### Response
```json
[
  {
    "course_id": 1,
    "course_level": 10300,
    "credits": 3,
    "description": "Intensive introduction to computing, tailored to the needs of those majoring in computer science and computer engineering. Introduction to programming in a modern object-oriented programming language such as C++, with particular emphasis on the logical evolution of working programs from specifications.",
    "name": "Introduction to Computing for Majors",
    "subject": "CSC"
  }
]
```

#### 3. Search for Courses
```http
GET /get_courses?q=intro
```
#### Response
```json
[
  {
    "course_id": 1,
    "course_level": 10300,
    "credits": 3,
    "description": "Intensive introduction to computing, tailored to the needs of those majoring in computer science and computer engineering. Introduction to programming in a modern object-oriented programming language such as C++, with particular emphasis on the logical evolution of working programs from specifications.",
    "name": "Introduction to Computing for Majors",
    "subject": "CSC"
  },
  {
    "course_id": 10,
    "course_level": 30400,
    "credits": 3,
    "description": "Finite state automata, pushdown automata, Turing Machines, and the languages they can recognize. Church\u2019s Thesis. Computibility. The classes P and NP; NP-complete and intractable problems.",
    "name": "Introduction to Theoretical Computer Science",
    "subject": "CSC"
  },
  {
    "course_id": 14,
    "course_level": 33600,
    "credits": 3,
    "description": "An introduction to database architecture. Levels of abstraction in a database system; physical database organization: abstract data models; relational databases and their query languages. Database design assignments.",
    "name": "Introduction to Database Systems",
    "subject": "CSC"
  },
  {
    "course_id": 24,
    "course_level": 48600,
    "credits": 3,
    "description": "An introduction to the performance and limitations of computer algorithms through a study of selected algorithms. Topics include primality testing and integer factorization, algorithms for integer programming and knapsack problems, reductions and NP-completeness, randomized algorithms, and experimental algorithms arising from new technologies such as molecular, neural, and quantum computing.",
    "name": "Introduction to Computational Complexity",
    "subject": "CSC"
  }
]
```

### Endpoint: `/get_professors`

### Parameters

- `q` (optional): A search query to filter professors by their name. This performs a partial match.
- `id` (optional): The professor ID to filter the professors. This performs an exact match.

### Example Requests and Response

#### 1. Retrieve all professors

```http
GET /get_professors
```
#### Response
```json
[
  [
    {
      "email": "manshel@ccny.cuny.edu",
      "id": 1,
      "name": "Michael Anshel"
    },
    {
      "email": "aarapi@ccny.cuny.edu",
      "id": 2,
      "name": "Albi Arapi"
    },
    {
      "email": "hauda@ccny.cuny.edu",
      "id": 3,
      "name": "Hesham Auda"
    },
    {
      "email": "navteniev@ccny.cuny.edu",
      "id": 4,
      "name": "Nikolai Avteniev"
    },
    {
      "email": "obetancourt@ccny.cuny.edu",
      "id": 5,
      "name": "Octavio Betancourt"
    },
  ...
]
```

#### 2. Retrieve a professor by ID
```http
GET /get_professors?id=44
```
#### Response
```json
[
  {
    "email": "wskeith@ccny.cuny.edu",
    "id": 44,
    "name": "William Skeith"
  }
]
```

#### 3. Search for Professors
```http
GET /get_professors?q=au
```
#### Response
```json
[
  {
    "email": "hauda@ccny.cuny.edu",
    "id": 3,
    "name": "Hesham Auda"
  },
  {
    "email": "apedersen@cs.ccny.cuny.edu",
    "id": 40,
    "name": "Arthur Paul Pedersen"
  },
  {
    "email": "ctaylor2@ccny.cuny.edu",
    "id": 47,
    "name": "Chaunce  Taylor"
  }
]
```

### Endpoint: `/get_sections`

### Parameters

- `section` (optional): The section ID to filter the courses. This performs an exact match.
- `course` (optional): The course ID to filter the courses. This performs an exact match.
- `professor` (optional): The professor ID to filter the courses. This performs an exact match.

### Example Requests and Response

#### 1. Retrieve all professors

```http
GET /get_sections
```
#### Response
```json
[
  {
    "course_code": "CSC 10300",
    "course_id": 1,
    "course_name": "Introduction to Computing for Majors",
    "credits": 3,
    "days": [
      {
        "day": "Fr",
        "end_time": "10:40:00",
        "start_time": "09:00:00"
      },
      {
        "day": "Mo",
        "end_time": "11:50:00",
        "start_time": "11:00:00"
      },
      {
        "day": "We",
        "end_time": "11:50:00",
        "start_time": "11:00:00"
      }
    ],
    "end_date": "2024-12-21",
    "instruction_mode": "In Person",
    "professors": [
      {
        "id": 7,
        "name": "Madeline Blount"
      },
      {
        "id": 59,
        "name": "Chunyu Yuan"
      }
    ],
    "rooms": [
      "NAC 7/107",
      "Marshak 117"
    ],
    "section_id": 30072,
    "start_date": "2024-08-28"
  },
  {
    "course_code": "CSC 10300",
    "course_id": 1,
    "course_name": "Introduction to Computing for Majors",
    "credits": 3,
    "days": [
      {
        "day": "Fr",
        "end_time": "12:40:00",
        "start_time": "11:00:00"
      },
      {
        "day": "Mo",
        "end_time": "11:50:00",
        "start_time": "11:00:00"
      },
      {
        "day": "We",
        "end_time": "11:50:00",
        "start_time": "11:00:00"
      }
    ],
    "end_date": "2024-12-21",
    "instruction_mode": "In Person",
    "professors": [
      {
        "id": 7,
        "name": "Madeline Blount"
      },
      {
        "id": 59,
        "name": "Chunyu Yuan"
      }
    ],
    "rooms": [
      "NAC 7/107",
      "Marshak 117"
    ],
    "section_id": 30073,
    "start_date": "2024-08-28"
  }
  ...
]
```

#### 2. Retrieve sections by section ID
```http
GET /get_sections?section=31823
```
#### Response
```json
[
  {
    "course_code": "CSC 10400",
    "course_id": 2,
    "course_name": "Discrete Mathematical Structures",
    "credits": 4,
    "days": [
      {
        "day": "Mo",
        "end_time": "15:40:00",
        "start_time": "14:00:00"
      },
      {
        "day": "We",
        "end_time": "15:40:00",
        "start_time": "14:00:00"
      },
      {
        "day": "Fr",
        "end_time": "10:40:00",
        "start_time": "09:00:00"
      }
    ],
    "end_date": "2024-12-21",
    "instruction_mode": "In Person",
    "professors": [
      {
        "id": 63,
        "name": "Tugce Ozdemir"
      }
    ],
    "rooms": [
      "TBA"
    ],
    "section_id": 31823,
    "start_date": "2024-08-28"
  }
]
```
#### 3. Retrieve sections by class ID
```http
GET /get_sections?course=5
```
#### Response
```json
[
  {
    "course_code": "CSC 21200",
    "course_id": 5,
    "course_name": "Data Structures",
    "credits": 3,
    "days": [
      {
        "day": "Mo",
        "end_time": "11:40:00",
        "start_time": "10:00:00"
      },
      {
        "day": "We",
        "end_time": "11:40:00",
        "start_time": "10:00:00"
      }
    ],
    "end_date": "2024-12-21",
    "instruction_mode": "Hybrid Synchronous",
    "professors": [
      {
        "id": 45,
        "name": "Yedidiah Solowiejczyk"
      }
    ],
    "rooms": [
      "TBA"
    ],
    "section_id": 32216,
    "start_date": "2024-08-28"
  },
  {
    "course_code": "CSC 21200",
    "course_id": 5,
    "course_name": "Data Structures",
    "credits": 3,
    "days": [
      {
        "day": "Tu",
        "end_time": "11:40:00",
        "start_time": "10:00:00"
      },
      {
        "day": "Th",
        "end_time": "11:40:00",
        "start_time": "10:00:00"
      }
    ],
    "end_date": "2024-12-21",
    "instruction_mode": "In Person",
    "professors": [
      {
        "id": 64,
        "name": "Weicong Feng"
      }
    ],
    "rooms": [
      "TBA"
    ],
    "section_id": 30076,
    "start_date": "2024-08-28"
  },
  {
    "course_code": "CSC 21200",
    "course_id": 5,
    "course_name": "Data Structures",
    "credits": 3,
    "days": [
      {
        "day": "Tu",
        "end_time": "15:40:00",
        "start_time": "14:00:00"
      },
      {
        "day": "Th",
        "end_time": "15:40:00",
        "start_time": "14:00:00"
      }
    ],
    "end_date": "2024-12-21",
    "instruction_mode": "In Person",
    "professors": [
      {
        "id": 60,
        "name": "Jianting Zhang"
      }
    ],
    "rooms": [
      "TBA"
    ],
    "section_id": 22079,
    "start_date": "2024-08-28"
  }
]
```

#### 3. Retrieve sections by professor ID
```http
GET /get_sections?professor=44
```
#### Response
```json
[
  {
    "course_code": "CSC 10300",
    "course_id": 1,
    "course_name": "Introduction to Computing for Majors",
    "credits": 3,
    "days": [
      {
        "day": "Fr",
        "end_time": "10:40:00",
        "start_time": "09:00:00"
      },
      {
        "day": "Tu",
        "end_time": "11:50:00",
        "start_time": "11:00:00"
      },
      {
        "day": "Th",
        "end_time": "11:50:00",
        "start_time": "11:00:00"
      }
    ],
    "end_date": "2024-12-21",
    "instruction_mode": "In Person",
    "professors": [
      {
        "id": 44,
        "name": "William Skeith"
      },
      {
        "id": 51,
        "name": "Martin Vasas"
      }
    ],
    "rooms": [
      "NAC 7/118",
      "Marshak MR3"
    ],
    "section_id": 30074,
    "start_date": "2024-08-28"
  },
  {
    "course_code": "CSC 10300",
    "course_id": 1,
    "course_name": "Introduction to Computing for Majors",
    "credits": 3,
    "days": [
      {
        "day": "Fr",
        "end_time": "12:40:00",
        "start_time": "11:00:00"
      },
      {
        "day": "Tu",
        "end_time": "11:50:00",
        "start_time": "11:00:00"
      },
      {
        "day": "Th",
        "end_time": "11:50:00",
        "start_time": "11:00:00"
      }
    ],
    "end_date": "2024-12-21",
    "instruction_mode": "In Person",
    "professors": [
      {
        "id": 44,
        "name": "William Skeith"
      },
      {
        "id": 51,
        "name": "Martin Vasas"
      }
    ],
    "rooms": [
      "NAC 7/118",
      "Marshak MR3"
    ],
    "section_id": 30075,
    "start_date": "2024-08-28"
  }
]
```