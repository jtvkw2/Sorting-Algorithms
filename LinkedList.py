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
        self.counters = {'data': 0, 'loop': 0, 'd_assign': 0, 'l_assign': 0, 'other': 0}

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
        self.counters['data'] += 1
        return self.head is None

    def size(self):
        self.counters['d_assign'] += 2
        current = self.head
        count = 0

        self.counters['l_assign'] += 1
        while current is not None:
            self.counters['loop'] += 1

            self.counters['d_assign'] += 2
            count = count + 1
            current = current.get_next()

        self.counters['data'] += 1
        return count

    def get_node(self, index):
        self.counters['d_assign'] += 2
        curr = self.head
        total = 0

        self.counters['l_assign'] += 1
        while curr:
            self.counters['loop'] += 1

            self.counters['data'] += 1
            if total == index:
                return curr

            self.counters['d_assign'] += 2
            total += 1
            curr = curr.next

    def selection_sort(self):
        t0 = time.time()

        self.counters['d_assign'] += 1
        temp = self.head

        self.counters['l_assign'] += 1
        while temp:
            self.counters['loop'] += 1

            self.counters['d_assign'] += 2
            smallest = temp
            r = temp.next

            self.counters['l_assign'] += 1
            while r:
                self.counters['loop'] += 1

                self.counters['data'] += 1
                if smallest.get_data() > r.get_data():
                    self.counters['d_assign'] += 1
                    smallest = r

                self.counters['d_assign'] += 1
                r = r.next

            self.counters['d_assign'] += 4
            x = temp.data
            temp.data = smallest.data
            smallest.data = x
            temp = temp.next

        t1 = time.time()
        total = t1 - t0
        run_items = [total, self.counters['data'], self.counters['loop'],
                     self.counters['d_assign'], self.counters['l_assign'], self.counters['other']]
        return run_items

    def bubble_sort(self):
        t0 = time.time()

        self.counters['d_assign'] += 1
        sort_one = None

        self.counters['data'] += 1
        if self.head is None:
            return

        self.counters['l_assign'] += 1
        while True:
            self.counters['loop'] += 1

            self.counters['d_assign'] += 2
            is_swapped = 0
            sort_two = self.head

            self.counters['l_assign'] += 1
            while sort_two.next != sort_one:
                self.counters['loop'] += 1

                self.counters['data'] += 1
                if sort_two.data > sort_two.next.data:
                    self.counters['d_assign'] += 3
                    sort_two.data, sort_two.next.data = sort_two.next.data, sort_two.data
                    is_swapped = 1

                self.counters['d_assign'] += 1
                sort_two = sort_two.next

            self.counters['d_assign'] += 1
            sort_one = sort_two

            self.counters['data'] += 1
            if is_swapped == 0:
                break

        t1 = time.time()
        total = t1 - t0
        run_items = [total, self.counters['data'], self.counters['loop'],
                     self.counters['d_assign'], self.counters['l_assign'], self.counters['other']]
        return run_items

    def insertion_sort(self):
        t0 = time.time()

        self.counters['data'] += 1
        if self.head is None:
            return
        else:
            self.counters['d_assign'] += 1
            current = self.head

            self.counters['l_assign'] += 1
            while current.next is not None:
                self.counters['loop'] += 1

                self.counters['d_assign'] += 1
                index = current.next

                self.counters['l_assign'] += 1
                while index is not None:
                    self.counters['loop'] += 1

                    self.counters['data'] += 1
                    if current.get_data() > index.get_data():
                        self.counters['d_assign'] += 3
                        temp = current.get_data
                        current.set_data = index.get_data
                        index.set_data = temp
                    self.counters['d_assign'] += 1
                    index = index.next
                self.counters['d_assign'] += 1
                current = current.next

        t1 = time.time()
        total = t1 - t0
        run_items = [total, self.counters['data'], self.counters['loop'],
                     self.counters['d_assign'], self.counters['l_assign'], self.counters['other']]
        return run_items

    def shell_sort(self):
        t0 = time.time()

        self.counters['d_assign'] += 2
        n = self.size()
        gap = n // 2

        self.counters['l_assign'] += 1
        while gap > 0:
            self.counters['loop'] += 1

            self.counters['l_assign'] += 1
            for i in range(gap, n):
                self.counters['loop'] += 1

                self.counters['d_assign'] += 2
                temp = self.get_node(i).data
                j = i

                self.counters['l_assign'] += 1
                while j >= gap and temp < self.get_node(j - gap).data:
                    self.counters['loop'] += 1

                    self.counters['d_assign'] += 2
                    self.get_node(j).set_data(self.get_node(j - gap).data)
                    j -= gap

                self.counters['d_assign'] += 1
                self.get_node(j).data = temp

            self.counters['d_assign'] += 1
            gap //= 2

        t1 = time.time()
        total = t1 - t0
        run_items = [total, self.counters['data'], self.counters['loop'],
                     self.counters['d_assign'], self.counters['l_assign'], self.counters['other']]
        return run_items

    def merge(self, h):
        self.counters['data'] += 1
        if h is None or h.next is None:
            return h

        self.counters['d_assign'] += 2
        center = self.get_middle(h)
        next_to_center = center.next

        self.counters['d_assign'] += 3
        center.next = None
        left = self.merge(h)
        right = self.merge(next_to_center)

        self.counters['data'] += 2
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def merge_sort(self, h):
        t0 = time.time()

        self.counters['data'] += 1
        self.merge(h)

        t1 = time.time()
        total = t1 - t0
        run_items = [total, self.counters['data'], self.counters['loop'],
                     self.counters['d_assign'], self.counters['l_assign'], self.counters['other']]
        return run_items

    def get_middle(self, h):
        self.counters['data'] += 1
        if h is None:
            return h

        self.counters['d_assign'] += 2
        slow = h
        runner = h

        self.counters['l_assign'] += 1
        while runner.next is not None and runner.next.next is not None:
            self.counters['loop'] += 1

            self.counters['d_assign'] += 2
            slow = slow.next
            runner = runner.next.next

        return slow

    def sorted_merge(self, a, b):
        self.counters['d_assign'] += 1
        end = None

        self.counters['data'] += 2
        if a is None:
            return b
        if b is None:
            return a

        self.counters['data'] += 1
        if a.data < b.data:
            self.counters['d_assign'] += 2
            end = a
            end.next = self.sorted_merge(a.next, b)
        else:
            self.counters['d_assign'] += 2
            end = b
            end.next = self.sorted_merge(a, b.next)
        return end

    def quick_sort(self):
        t0 = time.time()

        self.counters['data'] += 1
        self.quick_sort_helper(0, self.size() - 1)

        t1 = time.time()
        total = t1 - t0
        run_items = [total, self.counters['data'], self.counters['loop'],
                     self.counters['d_assign'], self.counters['l_assign'], self.counters['other']]
        return run_items

    def quick_sort_helper(self, a, b):
        self.counters['data'] += 1
        if a < b:
            self.counters['d_assign'] += 3
            split_point = self.partition(a, b)
            self.quick_sort_helper(a, split_point - 1)
            self.quick_sort_helper(split_point + 1, b)

    def partition(self, a, b):
        self.counters['d_assign'] += 4
        value = self.get_node(a).data
        l_mark = a + 1
        r_mark = b
        end = False

        self.counters['l_assign'] += 1
        while not end:
            self.counters['loop'] += 1

            self.counters['l_assign'] += 1
            while l_mark <= r_mark and self.get_node(l_mark).data <= value:
                self.counters['loop'] += 1
                self.counters['d_assign'] += 1
                l_mark = l_mark + 1

            self.counters['l_assign'] += 1
            while self.get_node(r_mark).data >= value and r_mark >= l_mark:
                self.counters['loop'] += 1
                self.counters['d_assign'] += 1
                r_mark = r_mark - 1

            self.counters['data'] += 1
            if r_mark < l_mark:
                self.counters['d_assign'] += 1
                end = True
            else:
                self.counters['d_assign'] += 3
                temp = self.get_node(l_mark).data
                self.get_node(l_mark).data = self.get_node(r_mark).data
                self.get_node(r_mark).data = temp

        self.counters['d_assign'] += 3
        temp = self.get_node(a).data
        self.get_node(a).data = self.get_node(r_mark).data
        self.get_node(r_mark).data = temp
        return r_mark
