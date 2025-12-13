# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
	# Write your code below this line
    result=[]
    for idx,task in enumerate(tasks,start=1):
        result.append(f"{idx}. {task}")
    return result
    pass