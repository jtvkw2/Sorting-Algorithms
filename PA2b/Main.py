from LinkedList import LinkedList
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    selection = []
    bubble = []
    insertion = []
    shell = []
    merge = []
    quick = []

    list_type = ["Ascending", "Descending", "Random"]
    list_num = ["500", "1000", "5000", "10000"]
    for y in range(3):
        for x in range(0, 4, 1):
            n = int(list_num[x // 4])
            if y == 0:
                data = np.arange(0, n, 1)
            elif y == 1:
                data = np.arange(n, 0, -1)
            else:
                data = np.random.randint(n, size=n)
            print("Generating Data For {} List".format(list_type[y]))
            ll = LinkedList()
            for i in range(n):
                ll.append(data[i])
            selection.append(ll.selection_sort())
            print("Selection sort N={} done".format(list_num[x % 4]))
            ll = LinkedList()
            for i in range(n):
                ll.append(data[i])
            bubble.append(ll.bubble_sort())
            print("Bubble sort N={} done".format(list_num[x % 4]))
            ll = LinkedList()
            for i in range(n):
                ll.append(data[i])
            insertion.append(ll.insertion_sort())
            print("Insertion sort N={} done".format(list_num[x % 4]))
            ll = LinkedList()
            for i in range(n):
                ll.append(data[i])
            shell.append(ll.shell_sort())
            print("Shell sort N={} done".format(list_num[x % 4]))
            ll = LinkedList()
            for i in range(n):
                ll.append(data[i])
            merge.append(ll.merge_sort(ll.head))
            print("Merge sort N={} done".format(list_num[x % 4]))
            ll = LinkedList()
            for i in range(n):
                ll.append(data[i])
            quick.append(ll.quick_sort())
            print("Quick sort N={} done\n".format(list_num[x % 4]))

    print("Making Selection Sort Output")
    output(selection, 'selection')
    print("Making Bubble Sort Output")
    output(bubble, 'bubble')
    print("Making Insertion Sort Output")
    output(insertion, 'insertion')
    print("Making Shell Sort Output")
    output(shell, 'shell')
    print("Making Merge Sort Output")
    output(merge, 'merge')
    print("Making Quick Sort Output")
    output(quick, 'quick')

    print("Creating Plots")
    plots(selection, bubble, insertion, shell, merge, quick)


def output(lists, sort_type):
    df = pd.DataFrame(lists, columns=["Seconds", "#Data", "#Loop", "#Data assignments",
                                      "#Loop Assignments", "# Other"])
    names = ["Sorted N=500", "Sorted N = 1000", "Sorted N=5000", "Sorted N=10000",
             "Descending sorted N=500", "Descending sorted N=1000", "Descending sorted N=5000",
             "Descending sorted N=10000", "Random N=500", "Random N=1000", "Random N=5000", "Random N=10000"]
    df.insert(loc=0, column="List configuration", value=names)
    df['Total'] = df.loc[:, '#Data':'# Other'].sum(1)
    print(df)
    df.to_csv('df_{}_sort_results.csv'.format(sort_type), index=False)
    print("Dataframe Saved \n")


def plots(selection, bubble, insertion, shell, merge, quick):
    list_type = ["Ascending Sorted", "Descending Sorted", "Random Unsorted"]
    for i in range(0, 6, 2):
        selection_rt_data = pd.Series([selection[i][0], selection[1 + i][0], selection[2 + i][0], selection[3 + i][0]],
                                      index=[500, 1000, 5000, 10000], name="Selection")
        bubble_rt_data = pd.Series([bubble[i][0], bubble[1 + i][0], bubble[2 + i][0], bubble[3 + i][0]],
                                   index=[500, 1000, 5000, 10000], name="Bubble")
        insertion_rt_data = pd.Series([insertion[i][0], insertion[1 + i][0], insertion[2 + i][0], insertion[3 + i][0]],
                                      index=[500, 1000, 5000, 10000], name="Insertion")
        shell_rt_data = pd.Series([shell[i][0], shell[1 + i][0], shell[2 + i][0], shell[3 + i][0]],
                                  index=[500, 1000, 5000, 10000], name="Shell")
        merge_rt_data = pd.Series([merge[i][0], merge[1 + i][0], merge[2 + i][0], merge[3 + i][0]],
                                  index=[500, 1000, 5000, 10000], name="Merge")
        quick_rt_data = pd.Series([quick[i][0], quick[1 + i][0], quick[2 + i][0], quick[3 + i][0]],
                                  index=[500, 1000, 5000, 10000], name="Quick")
        rt_data = [selection_rt_data, bubble_rt_data, insertion_rt_data, shell_rt_data, merge_rt_data, quick_rt_data]

        x_loc = np.arange(1, 5)
        x_labels = [500, 1000, 5000, 10000]
        f, ax = plt.subplots()
        ax.set_title("Runtime Plots for {} Type Array".format(list_type[i // 2]))
        ax.set_ylabel("Total Runtime")
        ax.set_xlabel("List size N")
        ax.set_xticks(x_loc)
        ax.set_xticklabels(x_labels)
        for rt in rt_data:
            plt.plot(x_loc, rt, label=rt.name)
        plt.legend(loc=0)
        plt.savefig("Plot_Time_{}.png".format(list_type[i // 2]))
        plt.show()
        plt.close(f)
        print("Created Plot {}".format(list_type[i // 2]))

    for i in range(0, 6, 2):
        selection_total_data = pd.Series(
            [sum(selection[i][1:5]), sum(selection[1 + i][1:5]), sum(selection[2 + i][1:5]),
             sum(selection[3 + i][1:5])], index=[500, 1000, 5000, 10000], name="Selection")
        bubble_total_data = pd.Series([sum(bubble[i][1:5]), sum(bubble[1 + i][1:5]), sum(bubble[2 + i][1:5]),
                                       sum(bubble[3 + i][1:5])], index=[500, 1000, 5000, 10000], name="Bubble")
        insertion_total_data = pd.Series(
            [sum(insertion[i][1:5]), sum(insertion[1 + i][1:5]), sum(insertion[2 + i][1:5]),
             sum(insertion[3 + i][1:5])], index=[500, 1000, 5000, 10000],
            name="Insertion")
        shell_total_data = pd.Series([sum(shell[i][1:5]), sum(shell[1 + i][1:5]), sum(shell[1 + i][1:5]),
                                      sum(shell[1 + i][1:5])], index=[500, 1000, 5000, 10000], name="Shell")
        merge_total_data = pd.Series([sum(merge[i][1:5]), sum(merge[1 + i][1:5]), sum(merge[1 + i][1:5]),
                                      sum(merge[1 + i][1:5])], index=[500, 1000, 5000, 10000], name="Merge")
        quick_total_data = pd.Series([sum(quick[i][1:5]), sum(quick[1 + i][1:5]), sum(quick[1 + i][1:5]),
                                      sum(quick[1 + i][1:5])], index=[500, 1000, 5000, 10000], name="Shell")
        total_data = [selection_total_data, bubble_total_data, insertion_total_data, shell_total_data, merge_total_data,
                      quick_total_data]

        x_loc = np.arange(1, 5)
        x_labels = [500, 1000, 5000, 10000]
        f, ax = plt.subplots()
        ax.set_title("Total Operation Plots for {} Type Array".format(list_type[i // 2]))
        ax.set_ylabel("Total Operation Count")
        ax.set_xlabel("List size N")
        ax.set_xticks(x_loc)
        ax.set_xticklabels(x_labels)
        for total in total_data:
            plt.plot(x_loc, total, label=total.name)
        plt.legend(loc=0)
        plt.savefig("Total_Operations_{}.png".format(list_type[i // 2]))
        plt.show()
        plt.close(f)
        print("Created Plot {}".format(list_type[i // 2]))


if __name__ == '__main__':
    main()
