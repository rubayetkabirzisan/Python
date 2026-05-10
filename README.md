# 🐍 100 Days of Python

A structured, day-by-day Python learning journal documenting progress through **~80+ concepts** — from bare-bones syntax to multithreading, async I/O, OOP design patterns, web scraping, and CLI tooling.

This repository tracks hands-on practice following the [CodeWithHarry 100 Days of Python](https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg) curriculum, with each day as a self-contained, runnable script.

---

## 📌 Why This Exists

Learning by doing. Every script in this repo was written from scratch — the goal was to understand *why* each construct works, not just *what* it does. Topics escalate deliberately: the same building blocks that appear in Day 10 (loops, conditionals) resurface in Day 39 (quiz game), Day 47 (encoder/decoder), and Day 98 (concurrent downloads) — showing how fundamentals compose into real programs.

---

## 🗂️ Repository Structure

```
Python-main/
│
├── Day 1/          # Hello World, first variable
├── Day 2–9/        # Core syntax: types, operators, typecasting, input
├── Day 10–15/      # Strings, slicing, built-in methods, time module
├── Day 16–19/      # Control flow: match/case, for/while, break/continue
├── Day 20–30/      # Functions: args, kwargs, recursion, scope
├── Day 31–35/      # Data structures: lists, tuples, sets
├── Day 36–38/      # Exception handling: try/except/finally, raise
├── Day 39–44/      # Projects + modules: quiz game, encoder, imports
├── Day 47–54/      # File I/O, lambdas, map/filter/reduce
├── Day 56–74/      # OOP: classes, inheritance, polymorphism, magic methods
├── Day 77–86/      # Advanced OOP, CLI tooling, operator overloading
├── Day 87–98/      # Concurrency: threading, asyncio, web scraping
│
├── myfile.txt      # Sample data used in file I/O exercises
├── sample.txt      # Sample data used in file seek/truncate exercises
└── requirements.txt
```

---

## 🧠 Concepts Covered

### 🔰 Foundations
| Day | Concept |
|-----|---------|
| 1–4 | Variables, `print()`, basic data types (`int`, `float`, `str`, `bool`, `complex`) |
| 5   | Escape sequences, `print()` separators and end characters |
| 6   | Lists, tuples, dictionaries — first look |
| 7–8 | Arithmetic and assignment operators |
| 9   | Typecasting — explicit (`int()`, `float()`) and implicit |
| 10  | `input()`, stdin handling, type conversion from user input |

### 📝 Strings
| Day | Concept |
|-----|---------|
| 11  | String indexing, iteration, concatenation |
| 12  | Slicing with positive and negative indices |
| 13  | 15+ string methods: `upper`, `lower`, `split`, `replace`, `find`, `index`, `count`, `startswith`, `endswith`, `isalpha`, `isalnum`, `isspace`, `swapcase`, `title`, `center` |
| 28  | `str.format()` and f-strings with format specifiers (e.g. `:.2f`) |

### 🔁 Control Flow
| Day | Concept |
|-----|---------|
| 14  | `if`, `elif`, `else` — including nested conditions |
| 15  | `time.strftime` for time-based branching |
| 16  | `match`/`case` (Python 3.10+ structural pattern matching) |
| 17  | `for` loops — strings, lists, `range()` with step |
| 18  | `while` loop with `else` clause |
| 19  | `break` and `continue` |

### ⚙️ Functions
| Day | Concept |
|-----|---------|
| 20  | Defining functions, return values, `pass` |
| 21  | Default args, `*args` (variadic positional), `**kwargs` (variadic keyword) |
| 29  | Docstrings — `__doc__` attribute |
| 30  | Recursion — factorial, Fibonacci (conceptual) |
| 48  | Variable scope — local vs global, `global` keyword |
| 52  | Lambda functions |
| 53  | Higher-order functions: `map()`, `filter()`, `reduce()` |
| 59  | Decorators — wrapping functions, preserving args with `*args/**kwargs` |
| 92  | `lru_cache` — memoization for expensive repeated calls |

### 🗄️ Data Structures
| Day | Concept |
|-----|---------|
| 22–23 | Lists — comprehensions, `sort`, `reverse`, `count`, `copy`, `insert`, `extend` |
| 24–25 | Tuples — immutability, `count()`, `index()` with start/end bounds |
| 31–32 | Sets — creation, `union`, `intersection`, `difference`, `symmetric_difference`, `issubset`, `issuperset`, `isdisjoint` |
| 33–34 | Dictionaries — `keys()`, `values()`, `items()`, `pop()`, `popitem()`, `update()` |

### 📂 File I/O
| Day | Concept |
|-----|---------|
| 49  | Reading and writing files — `open()`, modes (`r`, `w`, `a`), `with` statement |
| 50  | Parsing CSV-like text files line by line |
| 51  | `seek()`, `tell()`, `truncate()` for byte-level file control |

### 🚨 Error Handling
| Day | Concept |
|-----|---------|
| 36  | `try`/`except` — catching `ValueError`, `IndexError` |
| 37  | `finally` block — guaranteed execution regardless of outcome |
| 38  | `raise` — manually throwing exceptions with custom messages |

### 📦 Modules & Imports
| Day | Concept |
|-----|---------|
| 43–44 | `import`, `from x import y`, `import as`, `dir()`, `math` module |
| 3, 43 | Third-party imports: `pandas`, `hashlib` |

### 🏗️ Object-Oriented Programming
| Day | Concept |
|-----|---------|
| 56–57 | Classes, objects, class variables vs instance variables |
| 58   | `__init__` constructor |
| 60   | `@property` and `.setter` for encapsulated attribute access |
| 61–62 | Inheritance — `Programmer(Employee)`, protected members (`_name`) |
| 65   | `@staticmethod` — utility methods without `self` or `cls` |
| 66   | Class variables, `noOfEmployees` counter pattern |
| 69–70 | `@classmethod` — alternate constructors, class-level state mutation |
| 71   | `__dict__` introspection, `help()` |
| 72   | `super()` — calling parent `__init__` cleanly |
| 73   | Magic/dunder methods: `__str__`, `__repr__`, `__len__`, `__call__` |
| 74   | Method overriding + `super()` in multi-level inheritance |
| 77   | Operator overloading — `__add__` for a custom `Vector` class |
| 78–79 | Polymorphism (method overriding), multiple inheritance |
| 80   | MRO (Method Resolution Order) — `GoldenRetriever.mro()` |
| 81   | Hybrid and hierarchical inheritance patterns |

### ⚡ Advanced Python
| Day | Concept |
|-----|---------|
| 41  | Ternary operator |
| 42  | `enumerate()` with custom start index |
| 54  | `None` — identity check (`is`) vs equality (`==`) |
| 84  | `time.localtime()`, `time.strftime()`, performance timing |
| 85  | `argparse` — building a real CLI tool with positional + optional args |
| 86  | Walrus operator (`:=`, Python 3.8+) — assignment inside expressions |
| 87  | `shutil` + `os` — file/directory copy, move, remove, rmtree |
| 91  | Generators — `yield`, lazy evaluation, memory efficiency |
| 95  | Regular expressions — `re.search`, `re.finditer`, character classes, anchors |

### 🔄 Concurrency & Networking
| Day | Concept |
|-----|---------|
| 89  | Web scraping — `requests` + `BeautifulSoup`, parsing HTML, extracting tags |
| 96  | `asyncio` — `async def`, `await`, `asyncio.gather()` for concurrent HTTP |
| 97  | Threading — `threading.Thread`, `ThreadPoolExecutor`, `executor.map()` |
| 98  | Multiprocessing — `ProcessPoolExecutor`, concurrent file downloading |

---

## 🚀 Notable Programs

### 🎮 KBC Quiz Game — Day 39
A terminal recreation of *Kaun Banega Crorepati* (Who Wants to Be a Millionaire). Manages a question bank, prize ladder, quit-and-bank logic, and lifeline milestones. Demonstrates list-of-lists data modelling, loop control, f-string formatting, and stateful game logic — entirely in the standard library.

### 🔐 Secret Code Encoder/Decoder — Day 47
A two-way string cipher. Short words are reversed; longer words have their first character rotated to the end with fixed random pads appended. Decoding reverses the exact transformation. Shows string slicing, join/split patterns, and conditional branching on string length.

### 📥 CLI File Downloader — Day 85
A proper command-line tool built with `argparse`. Accepts a URL as a positional argument and an optional `-o`/`--output` filename flag. Streams large files in chunks using `requests` to avoid loading the full response into memory — a real-world pattern used in production download utilities.

```bash
python main.py https://example.com/image.jpg -o output.jpg
```

### 🕸️ Web Scraper — Day 89
Fetches a live webpage, parses the full HTML tree with `BeautifulSoup`, and extracts all `<h2>` headings. Includes a commented-out `POST` request example against a JSON API. Demonstrates real HTTP interaction against a live server, not mocked data.

### ⚡ Concurrent Image Downloader — Day 98
Downloads 60 images in parallel using `ProcessPoolExecutor`. Handles directory creation, binary file writing, and exception isolation per worker — a realistic pattern for batch data-fetching pipelines.

---

## 🛠️ Setup & Usage

**Requirements:** Python 3.8+ (Days 86+), Python 3.10+ for `match`/`case` (Day 16)

**Install dependencies:**
```bash
pip install requests beautifulsoup4 pandas
```

**Run any day's script:**
```bash
cd "Day 39"
python main.py
```

**CLI tool (Day 85):**
```bash
cd Day_85
python main.py https://picsum.photos/800/600 -o photo.jpg
```

---

## 📈 Learning Progression

```
Days  1–20  ▓▓▓▓▓░░░░░░░░░░░░░░░  Syntax, types, control flow, functions
Days 21–40  ░░░░▓▓▓▓▓░░░░░░░░░░░  Data structures, recursion, first projects
Days 41–60  ░░░░░░░░▓▓▓▓▓░░░░░░░  File I/O, modules, lambdas, decorators
Days 61–80  ░░░░░░░░░░░░▓▓▓▓▓░░░  Full OOP — inheritance, polymorphism, dunder methods
Days 81–98  ░░░░░░░░░░░░░░░░▓▓▓▓  Concurrency, CLI, async, regex, web scraping
```

---

## 🔧 Tech Stack

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![requests](https://img.shields.io/badge/requests-HTTP-orange)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-Scraping-green)
![asyncio](https://img.shields.io/badge/asyncio-Async-purple)
![threading](https://img.shields.io/badge/threading-Concurrent-red)

---

