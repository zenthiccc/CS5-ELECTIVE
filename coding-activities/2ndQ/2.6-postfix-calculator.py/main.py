import my_queue
import my_stack

# evaluates an arithmetic expression in postfix notation
def eval_postfix_exp(exp_string):
  try:
    exp_queue = exp_string_to_exp_queue(exp_string)
    stack = my_stack.Stack()
    length = exp_queue.items.length()
    num3 = 0
    for i in range(length):
      item = exp_queue.dequeue()
      if isinstance(item, float):
        stack.push(item)
      else:
        num1 = stack.pop()
        num2 = stack.pop()
        if item == "+":
          num3 = num2 + num1
        elif item == "-":
          num3 = num2 - num1
        elif item == "*":
          num3 = num2 * num1
        elif item == "/":
          num3 = num2 / num1
        elif item == "//":
          num3 = num2 // num1
        elif item == "%":
          num3 = num2 % num1
        stack.push(num3)
    if stack.items.length() != 1:
      #this error will be captured by the try except
      quit()
    return num3

  except:
    return "invald input"
# converts an expresssion string into a queue of terms/integers and operations
def exp_string_to_exp_queue(exp_string): 
    exp_queue = my_queue.Queue()
    temporary = ''
    counter = 0
    size = len(exp_string)
    operation = ('+', '-', '*', '/', '//', '%')
    for item in exp_string:
      counter += 1
      temporary = ''.join(temporary.split())
      #execute if have space
      if item.isspace():
        #print('space')
        if temporary in operation:
          exp_queue.enqueue(temporary)
        else:
          exp_queue.enqueue(float(temporary))
        temporary = ''
      #execute if last item
      if counter == size:
        if item not in operation:
          #this error will be captured by the try except
          quit()
        else:
          temporary += item
          exp_queue.enqueue(temporary)
          temporary = ''  
      else:
        temporary += item
    return exp_queue
    