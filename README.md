# Task management system

## Coding exercise:

Create a simple task management application with the following features:
- A backend API (Python) that allows creating, reading, updating, and deleting tasks
- A frontend (HTML, CSS, vanilla JavaScript) that displays tasks and allows user interaction
- Tasks should have a title, description, due date, and status (e.g., pending, in progress, completed)

Focus on:
- Implementing CRUD operations
- Proper error handling
- Basic styling and layout
- Event handling in JavaScript
- Efficient data structures (e.g., for sorting tasks by due date)

## System design exercise

Extend the task management application to handle the following scenarios:

1. Scalability:
    - How would you modify the system to handle millions of users and tasks?
    - Implement caching to reduce database load
    - Design a load balancing solution

2. Real-time updates:
    - Add functionality for real-time task updates across multiple users
    - Consider using WebSockets or long-polling

3. Authentication and Authorization:
    - Implement a user authentication system
    - Add role-based access control (e.g., admin, regular user)

4. Analytics:
    - Design a system to track and analyze user activity and task completion rates
    - Consider how to handle large amounts of analytics data

5. Mobile app integration:
    - How would you modify your backend to support both web and mobile clients?

6. Offline functionality:
    - Design a solution for users to work offline and sync when back online

For each scenario, practice:
- Drawing system architecture diagrams
- Explaining your design choices
- Discussing trade-offs between different approaches
- Considering non-functional requirements (scalability, maintainability, extensibility)

Remember to practice explaining your thought process out loud as you work through these exercises. This will help you communicate effectively during the interview.

Also, be prepared to discuss topics like:
- RESTful API design
- Database choices (SQL vs NoSQL)
- Caching strategies
- Message queues for asynchronous processing
- Monitoring and alerting systems
- Microservices architecture

## Running the application

Run this application with:
```bash 
uvicorn backend/main:app --reload
```