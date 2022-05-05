import unittest
import csv
import math
from collections import Counter

from MyCalc import MyCalc

class AdvCalc(MyCalc):

    def square(self, a):
        ans = a*a
        print("Square of {} = {}".format(a, ans))
        return ans

    def square_root(self, a):
        ans = math.sqrt(a)
        print("Square root of {} = {}".format(a, ans))
        return ans

    def mean(self, *args, **kwargs):
        if args:
            data = list(args)
        else:
            data = kwargs.get('data', [])
        sum_of_data = sum(data)
        num = len(data)
        mean = sum_of_data/num
        print("Mean of given list {} is : {}".format(data, mean))
        return mean

    def median(self, *args, **kwargs):
        if args:
            data = list(args)
        else:
            data = kwargs.get('data', [])

        data.sort()
        mid = len(data)// 2
        median = (data[mid] + data[~mid]) / 2
        print("Median of given list {} is : {}".format(data, median))
        return median

    def mode(self, *args, **kwargs):
        if args:
            data = list(args)
        else:
            data = kwargs.get('data', [])

        num = len(data)
        count_occurence = Counter(data)
        mode = [k for k, v in count_occurence.items() if v == max(list(count_occurence.values()))]
        if len(mode) == num:
            get_mode = "No mode found"
        else:
            get_mode = ', '.join(map(str, mode))
        print("Mode of given list {} is : {}".format(data, get_mode))
        return get_mode

    def standard_deviation(self, *args, **kwargs):
        if args:
            data = list(args)
        else:
            data = kwargs.get('data', [])

        mean = self.mean(*args)
        diffs = [(d - mean)**2 for d in data]
        sum_diff = sum(diffs)
        ans = (sum_diff / (len(data) - 1)) ** 0.5
        print("Standard deviation of given list {} is :{}".format(data, ans))
        return ans

    def z_score(self, *args, **kwargs):
        if args:
            data = list(args)
        else:
            data = kwargs.get('data', [])

        mean = self.mean(*args)
        std_dev = self.standard_deviation(*args)
        zscores = [(d - mean) / std_dev for d in data]
        print("z score for {} is : {}".format(data, zscores))
        return zscores

obj = AdvCalc()
import pdb;pdb.set_trace()

class TestAdvCalc(unittest.TestCase):
    def test_addition(self):
        adv_cal = AdvCalc()
        with open("Unity_Test_Addition.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()#skiping header row
            for row in csv_reader:
                v1 = int(row[0])
                v2 = int(row[1])
                ans = int(row[2])
                adv_cal.run(v1, "+", v2)
                self.assertEqual(adv_cal.ans, ans)

    def test_multiply(self):
        adv_cal = AdvCalc()
        with open("Unit_Test_Multiplication.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()#skiping header row
            for row in csv_reader:
                v1 = int(row[0])
                v2 = int(row[1])
                ans = int(row[2])
                adv_cal.run(v1, "*", v2)
                self.assertEqual(adv_cal.ans, ans)

    def test_division(self):
        adv_cal = AdvCalc()
        with open("Unit_Test_Division.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()#skiping header row
            for row in csv_reader:
                v1 = int(row[0])
                v2 = int(row[1])
                ans = float(row[2])
                adv_cal.run(v2, "/", v1)
                self.assertEqual(adv_cal.ans, ans)

    def test_subtraction(self):
        adv_cal = AdvCalc()
        with open("Unit_Test_Subtractions.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()#skiping header row
            for row in csv_reader:
                v1 = int(row[0])
                v2 = int(row[1])
                ans = int(row[2])
                adv_cal.run(v2, "-", v1)
                self.assertEqual(adv_cal.ans, ans)

    def test_square(self):
        adv_cal = AdvCalc()
        with open("Unit_Test_Square.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()#skiping header row
            for row in csv_reader:
                v1 = int(row[0])
                ans = int(row[1])
                actual = adv_cal.square(v1)
                self.assertEqual(actual, ans)

    def test_square_root(self):
        adv_cal = AdvCalc()
        with open("Unit_Test_Square_Root.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()#skiping header row
            for row in csv_reader:
                v1 = int(row[0])
                ans = float(row[1])
                actual = adv_cal.square_root(v1)
                self.assertEqual(actual, ans)
    def test_mean(self):
        adv_cal = AdvCalc()
        self.assertEqual(adv_cal.mean(1,2,3), 2)

    def test_median(self):
        adv_cal = AdvCalc()
        self.assertEqual(adv_cal.median(1,2,3), 2)

    def test_mode(self):
        adv_cal = AdvCalc()
        self.assertEqual(adv_cal.mode(1,2,3,3), '3')
        self.assertEqual(adv_cal.mode(1,2,3), "No mode found")

    def test_standard_deviation(self):
        adv_cal = AdvCalc()
        self.assertEqual(adv_cal.standard_deviation(1,2,3), 1.0)

    def test_zscore(self):
        adv_cal = AdvCalc()
        self.assertEqual(adv_cal.z_score(1,2,3), [-1.0, 0.0, 1.0])

