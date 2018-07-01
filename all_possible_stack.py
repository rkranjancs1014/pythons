def subset_using_stack_queue(elements):
    input_stack = ArrayStack()
    output_queue = ArrayQueue()
    intermediate_stack = ArrayStack()
    output_queue.enqueue([])
    input_stack.push([])
    for ele in elements:
        while(not input_stack.is_empty()):
            pop_list = input_stack.pop()
            intermediate_stack.push(pop_list)
        while(not intermediate_stack.is_empty()):
            sub_list = intermediate_stack.pop()
            input_stack.push(sub_list)
            new_list = [i for i in sub_list]
            new_list.append(ele)
            output_queue.enqueue(new_list)
            input_stack.push(new_list)
    return output_queue
