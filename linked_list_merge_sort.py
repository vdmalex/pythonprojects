from linked_list import LinkedList 




def merge_sort(linked_list):
    """
    sorts a linked list ina  ascending order
    recurisvely ivide the linked list into sublists containing a single node
    repeatedliy merge the sublist to produce sorted sublistt until one remains
    returns a sorted linked list
    Takes O(kn log n)
    """
    if linked_list.size()==1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half,right_half=split(linked_list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    
    return merge(left,right)
    

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(kn log n)
    """

    if linked_list==None or linked_list.head==None:
        left_half=linked_list
        right_half=None

        return left_half,right_half

    else:
        size=linked_list.size()
        mid=size//2
        
        mid_node=linked_list.node_at_index(mid-1)
        
        left_half=linked_list
        right_half=LinkedList()
        right_half.head=mid_node.next_node      #mid node+1
        mid_node.next_node=None                 #mid node has no next node

        return left_half,right_half

def merge(left,right):
    """
    Merges two linked lists, sorting by data in the nodes
    Returns a new, merged list
    """
    # create a new linked list that contiains nodes from
    # merging left and right
    merged=LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)
    # set current to the head of the linked list
    current=merged.head

    # obtain head nodes for left and right linked lists
    left_head=left.head
    right_head=right.head

    # iterate over left and until we reach the tail node of either

    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # add the ndoe from right to merged linked list
        if left_head is None:
            current.next_node=right_head
            # call next on right to set loop condition to False
            right_head=right_head.next_node
            # If the head node of the right is None, we're past the tail
            # Add the tail node form left ot merged linked list
        elif right_head is None:
            current.next_node=left_head
            # call next on left to set loop condition to False
            left_head=left_head.next_node
        else:
            # Not at either tail node 
            # obtain node data to perform comparison operations
            left_data=left_head.data
            right_data=right_head.data
            # If data on left is less that right, set current to elft node
            if left_data< right_data:
                current.next_node = left_head#move left head ot next node
                left_head=left_head.next_node
            # if data on left is greater than right, set current to right node
            else:
                current.next_node=right_head
                # move right head to next node
                right_head=right_head.next_node
        # move current to next node
        current=current.next_node
        
    # Discard fake head and set first merged node as head
    head=merged.head.next_node
    merged.head=head
    return merged


l=LinkedList()
l.add(10)
l.add(12)
l.add(23)
l.add(643)
l.add(32)
l.add(1)
l.add(7)

print(l)
sorted_linked_list=merge_sort(l)
print(sorted_linked_list)

            


    

