# 反转链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

if __name__ == '__main__':
    res = ListNode.reverseList(["abc","123","def","456"])
    print(res)
