#!/usr/bin/python3

def generate_readme():
    title = input("Enter the title of the README: ")
    topic = input("Enter the topic: ")
    
    resources = []
    num_resources = int(input("Enter the number of resources: "))
    for i in range(num_resources):
        resource = input(f"Enter resource {i+1}: ")
        resources.append(resource)
    
    learning_objectives = []
    num_objectives = int(input("Enter the number of learning objectives: "))
    for i in range(num_objectives):
        objective = input(f"Enter learning objective {i+1}: ")
        learning_objectives.append(objective)
    
    tasks = []
    num_tasks = int(input("Enter the number of tasks: "))
    for i in range(num_tasks):
        task_title = input(f"Enter title for task {i+1}: ")
        task_description = input(f"Enter description for task {i+1}: ")
        task_prototype = input(f"Enter prototype for task {i+1}: ")
        task_additional_notes = input(f"Enter additional notes for task {i+1}: ")
        
        task = {
            "title": task_title,
            "description": task_description,
            "prototype": task_prototype,
            "additional_notes": task_additional_notes
        }
        tasks.append(task)
    
    readme_content = f"# {title}\n\n{topic}\n\n## Resources\n\n"
    for resource in resources:
        readme_content += f"- {resource}\n"
    readme_content += "\n## Learning Objectives\n\n"
    for objective in learning_objectives:
        readme_content += f"- {objective}\n"
    readme_content += "\n## Tasks\n\n"
    for i, task in enumerate(tasks, start=1):
        readme_content += f"{i}. {task['title']}\n\n"
        readme_content += f"{task['description']}\n\n"
        readme_content += "Prototype:\n\n```python\n"
        readme_content += f"{task['prototype']}\n```\n\n"
        readme_content += f"{task['additional_notes']}\n\n"

    return readme_content


readme_content = generate_readme()

# Write the README content to a file
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("README.md file generated successfully!")
