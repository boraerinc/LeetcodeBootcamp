# Week 3 Homework Problems

# 876. Middle of the Linked List

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    s, f = head, head

     while f is not None and f.next is not None:
        s = s.next
        f = f.next.next

     return s

# 36. Valid Sudoku
def isValidSudoku(self, board):
    dic = set()
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val != '.':
                row_key = (r, val)
                col_key = (val, c)
                box_key = (r // 3, c // 3, val)
                if row_key in dic or col_key in dic or box_key in dic:
                    return False
                
                dic.add(row_key)
                dic.add(col_key)
                dic.add(box_key)
    return True

# 25. Reverse Nodes in k-Group

def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        for i in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        
        prev, curr = kth.next, group_prev.next
        
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        temp = group_prev.next
        group_prev.next = prev
        group_prev = temp
    return dummy.next
