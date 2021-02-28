import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        list_str = ""
        curr = self.head
        while curr is not None:
            list_str += str(curr)
            list_str += "->"
            curr = curr.get_next()
        list_str += "None"
        return list_str

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def append(self, item):
        curr = self.head
        if self.head is None:
            self.head = Node(item)
        else:
            while curr.get_next() is not None:
                curr = curr.get_next()
            temp = Node(item)
            curr.set_next(temp)
            temp.set_prev(curr)

    def insert(self, index, item):
        if index == 0:
            self.add(item)
        else:  # not adding at front. stop one before location
            curr = self.head
            i = 0
            while curr.get_next() is not None and i < index - 1:
                curr = curr.get_next()
                i += 1
            temp = Node(item)
            temp.set_next(curr.get_next())
            curr.set_next(temp)

    def pop(self, index=None):
        if index is None:
            index = self.size() - 1

        if index == 0:
            curr = self.head
            self.head = self.head.get_next()
            return curr
        else:  # not popping front. stop one before location
            curr = self.head
            i = 0
            while curr.get_next() is not None and i < index - 1:
                curr = curr.get_next()
                i += 1
            to_pop = curr.get_next()
            curr.set_next(to_pop.get_next())
            return to_pop

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = -1
        loc = 0
        while current is not None and found == -1:
            if current.get_data() == item:
                found = loc
            else:
                current = current.get_next()
            loc += 1

        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def get_node(self, index):
        curr = self.head
        total = 0
        while curr:
            if total == index:
                return curr
            total += 1
            curr = curr.next

    def selection_sort(self):
        data, loop, d_assign, l_assign, other = 0, 0, 0, 0, 0
        t0 = time.time()

        d_assign += 1
        temp = self.head

        l_assign += 1
        while temp:
            loop += 1

            d_assign += 2
            smallest = temp
            r = temp.next

            l_assign += 1
            while r:
                loop += 1

                data += 1
                if smallest.get_data() > r.get_data():
                    d_assign += 1
                    smallest = r

                d_assign += 1
                r = r.next

            d_assign += 4
            x = temp.data
            temp.data = smallest.data
            smallest.data = x
            temp = temp.next

        t1 = time.time()
        total = t1 - t0
        run_items = [total, data, loop, d_assign, l_assign, other]
        return run_items

    def bubble_sort(self):
        data, loop, d_assign, l_assign, other = 0, 0, 0, 0, 0
        t0 = time.time()

        d_assign += 1
        sort_one = None

        data += 1
        if self.head is None:
            return

        l_assign += 1
        while True:
            loop += 1

            d_assign += 2
            is_swapped = 0
            sort_two = self.head

            l_assign += 1
            while sort_two.next != sort_one:
                loop += 1

                data += 1
                if sort_two.data > sort_two.next.data:
                    d_assign += 3
                    sort_two.data, sort_two.next.data = sort_two.next.data, sort_two.data
                    is_swapped = 1

                d_assign += 1
                sort_two = sort_two.next

            d_assign += 1
            sort_one = sort_two

            data += 1
            if is_swapped == 0:
                break

        t1 = time.time()
        total = t1 - t0
        run_items = [total, data, loop, d_assign, l_assign, other]
        return run_items

    def insertion_sort(self):
        data, loop, d_assign, l_assign, other = 0, 0, 0, 0, 0
        t0 = time.time()

        data += 1
        if self.head is None:
            return
        else:
            d_assign += 1
            current = self.head

            l_assign += 1
            while current.next is not None:
                loop += 1

                d_assign += 1
                index = current.next

                l_assign += 1
                while index is not None:
                    loop += 1

                    data += 1
                    if current.get_data() > index.get_data():
                        d_assign += 3
                        temp = current.get_data
                        current.set_data = index.get_data
                        index.set_data = temp
                    d_assign += 1
                    index = index.next
                d_assign += 1
                current = current.next

        t1 = time.time()
        total = t1 - t0
        run_items = [total, data, loop, d_assign, l_assign, other]
        return run_items

    def shell_sort(self):
        data, loop, d_assign, l_assign, other = 0, 0, 0, 0, 0
        t0 = time.time()

        d_assign += 2
        n = self.size()
        gap = n // 2

        l_assign += 1
        while gap > 0:
            loop += 1

            l_assign += 1
            for i in range(gap, n):
                loop += 1

                d_assign += 2
                temp = self.get_node(i).data
                j = i

                l_assign += 1
                while j >= gap and temp < self.get_node(j - gap).data:
                    loop += 1

                    d_assign += 2
                    self.get_node(j).set_data(self.get_node(j - gap).data)
                    j -= gap

                d_assign += 1
                self.get_node(j).data = temp

            d_assign += 1
            gap //= 2

        t1 = time.time()
        total = t1 - t0
        run_items = [total, data, loop, d_assign, l_assign, other]
        return run_items
