# Project Management Glossary

## **Basic Building Blocks**

### **Task**
- **What it is:** A single piece of work that one person can complete
- **Example:** "Write a function that reads a file" or "Add a login button"
- **Size:** Usually takes a few hours to a few days
- **Think of it as:** One item on your to-do list

### **Goal** 
- **What it is:** What you want to achieve or accomplish
- **Example:** "Make the app work on mobile phones" or "Users can save their work"
- **Size:** Bigger than a task, made up of multiple tasks
- **Think of it as:** The destination you're trying to reach

### **Phase**
- **What it is:** A major chunk of the project with related work
- **Example:** "Phase 1: Basic Features" → "Phase 2: Make it Pretty" → "Phase 3: Test Everything"
- **Size:** Usually 1-4 weeks of work
- **Think of it as:** Chapters in a book - each has a theme

## **Quality Control Terms**

### **Entry Criteria**
- **What it is:** Things that MUST be ready before you can start this phase/task
- **Example:** "Python must be installed" or "Previous phase must be 100% done"
- **Purpose:** Prevents you from starting something you can't finish
- **Think of it as:** "You must be this tall to ride" - requirements to begin

### **Exit Criteria**
- **What it is:** Things that MUST be finished before you can move to the next phase/task
- **Example:** "All tests pass" or "App works on 3 different computers"
- **Purpose:** Prevents you from declaring something "done" when it's not really done
- **Think of it as:** "Graduation requirements" - what you need to move forward

### **Acceptance Criteria**
- **What it is:** Specific, testable conditions that prove a task is complete
- **Example:** "When user clicks 'Save', the file appears in the folder"
- **Purpose:** Everyone agrees on what "done" looks like
- **Think of it as:** "Definition of done" - no arguing about whether it works

## **Progress Tracking Terms**

### **Milestone**
- **What it is:** A major achievement or checkpoint in your project
- **Example:** "Version 1.0 Released" or "Beta Testing Complete"
- **Size:** Usually marks the end of a phase
- **Think of it as:** Mile markers on a highway - shows how far you've come

### **Quality Gate**
- **What it is:** A checkpoint where you verify quality before moving forward
- **Example:** "All code must be reviewed" or "Performance must be under 2 seconds"
- **Purpose:** Catches problems early instead of at the end
- **Think of it as:** Security checkpoint - you can't pass without meeting standards

### **Dependency**
- **What it is:** Something that must happen before this task can be completed
- **Example:** "Task B can't start until Task A is finished" or "Need API keys before testing"
- **Purpose:** Shows the order things must happen in
- **Think of it as:** Recipe steps - you can't bake before you mix

## **Risk Management Terms**

### **Risk**
- **What it is:** Something that might go wrong and hurt your project
- **Example:** "The external API might be unreliable" or "Developer might get sick"
- **Levels:** High (very likely to happen), Medium (might happen), Low (probably won't happen)
- **Think of it as:** Storm clouds on the horizon - problems you can see coming

### **Mitigation**
- **What it is:** Your plan to prevent the risk or reduce its impact
- **Example:** If API fails → "Have a backup data source ready"
- **Purpose:** Being prepared instead of surprised
- **Think of it as:** Umbrella for the storm - your protection plan

### **Contingency Plan**
- **What it is:** Your backup plan if the risk actually happens
- **Example:** If main approach fails → "Switch to simpler approach"
- **Purpose:** Know what to do if things go wrong
- **Think of it as:** Plan B (or Plan C) - alternative routes to your destination

## **Status Terms**

### **Not Started**
- **What it means:** Haven't begun this work yet
- **When to use:** Task is planned but no code written yet

### **In Progress** 
- **What it means:** Currently working on this task
- **When to use:** Code is being written, tests are being run

### **Complete**
- **What it means:** Task is finished and meets all acceptance criteria
- **When to use:** Everything works and has been tested

### **Blocked**
- **What it means:** Can't continue because waiting for something else
- **When to use:** Stuck waiting for information, tools, or another task

## **Real-World Example**

**Project:** Build a calculator app

**Phase 1 Goal:** Basic math works  
**Entry Criteria:** Have a computer, know how to code  
**Tasks:**
- Task 1: Create buttons for numbers (0-9)
- Task 2: Create buttons for operations (+, -, ×, ÷)
- Task 3: Make buttons actually calculate

**Acceptance Criteria for Task 1:** "When user clicks '5', the number 5 appears on screen"

**Exit Criteria for Phase 1:** "Calculator can do 2+2=4 without crashing"

**Risk:** "What if I don't know how to handle division by zero?"  
**Mitigation:** "Research error handling before starting division feature"  
**Contingency:** "If it's too hard, show 'Error' message instead of crashing"

**Quality Gate:** "All math must be tested with at least 10 different calculations"

## **Why Use This Language?**

**Without structure:**
- "I'm working on stuff"
- "It's mostly done" 
- "Should be ready soon"

**With structure:**
- "I'm in Phase 2, Task 3 is in progress"
- "Phase 1 exit criteria are 100% met"
- "Milestone 2 will be complete when all quality gates pass"

The structured language helps everyone (including future you) understand exactly where the project stands and what needs to happen 