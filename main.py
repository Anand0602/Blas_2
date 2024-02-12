import numpy as np

class BLAS_2:
    
    def __init__(self, rows, cols, alpha, A):

            self.rows = rows
            self.cols = cols
            self.alpha = alpha
            self.A = A
            
    def matrix_vector(self):
        
        matrix_a = [] # Initialize matrix
        print("Enter the Entries:")

        for i in range(self.rows):
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            matrix_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_a[i][j], end=" ")
            print()

        print("Matrix A = \n",matrix_a)

        vector_size = int(input("enter size of vector: "))

        vector=[]
        print("enter entries")
        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res = np.dot(matrix_a, vector)

        print(" --------- Matrix multiplication: ------------ ")
        print("The Result: ")
        print(final_res)

# -----------------------------------------------------------------------------------------------------------------------------

    def symmetric_matrix_vector(self):
        print("----------------------------------------------------")
        print("SYMMETRIC MATRIX VECTOR MULTIPLY")
        print("----------------------------------------------------")

        matrix_sym_a = []

        print("Enter the Entries:")

        for i in range(self.rows):         
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n",matrix_sym_a)

        def symmetric(row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if(i < j or i >j):
                        matrix_sym_a[i][j] = matrix_sym_a[j][i]
                
        print("Symmetric Matrix: ")
        symmetric(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n",matrix_sym_a)

        vector_size = int(input("enter size of vector"))

        vector=[]
        print("enter entries for vector:")

        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_sym_res = np.dot(matrix_sym_a, vector)

        print("\nMatrix multiplication: ")
        print("The Result")
        print(final_sym_res)
        
# -----------------------------------------------------------------------------------------------------------------------------

    def triangular_matrix_vector(self):
        print("------------------------------------------")
        print("TRAINGULAR MATRIX VECTOR MULTIPLY")
        print("------------------------------------------")

        matrix_sym_a = []

        print("Enter the Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n", matrix_sym_a)

        def lower(matrix, row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if (i < j):
                        print("0", end=" ")
                        matrix_sym_a[i][j] = (0)
                    else:
                        print(matrix[i][j],end=" ")
                        matrix_sym_a[i][j] = matrix[i][j]
                print(" ")
                
        print("Triangular matrix: ")
        lower(matrix_sym_a, self.rows, self.cols)
        print(matrix_sym_a)

        vector_size = int(input("enter size of vector"))

        vector=[]
        print("enter entries vector entries: ")

        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res = np.dot(matrix_sym_a, vector)

        print("The Result: ")
        print(final_res)

# -----------------------------------------------------------------------------------------------------------------------------
        
    def triangular_banded_matrix_vector(self):
        print("------------------------------------------")
        print("TRIANGULAR BANDED MATRIX MULTIPLICATION")
        print("------------------------------------------")

        #============== MATRIX A ================

        matrix_sym_a = []

        print("Enter the Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n", matrix_sym_a)

        k = 1
        def lower(matrix, row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if (i < j):
                        print("0", end=" ")
                        matrix_sym_a[i][j] = (0)
                    else:
                        print(matrix[i][j],end=" ")
                        matrix_sym_a[i][j] = matrix[i][j]
                        
                        if i-j>k:
                            matrix_sym_a[i][j] = 0
                print(" ")

        print("Triangular matrix: ")
        lower(matrix_sym_a, self.rows, self.cols)
        print(matrix_sym_a)

        vector_size = int(input("enter size of vector"))

        vector=[]
        print("enter entries vector entries: ")

        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res = np.dot(matrix_sym_a, vector)

        print("The Result: ")
        print(final_res)
        
# -----------------------------------------------------------------------------------------------------------------------------

    def Rank_1_operation(self):
        print("------------------------------------------")
        print("RANK 1 OPERATION")
        print("------------------------------------------")

        # =============== VALUE OF A ===============

        A = []          # Initialize matrix

        print("Enter the Row wise Entries:") 

        for i in range(self.rows):         
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            A.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end = " ")
            print()
            
        print("Matrix A = \n",A)

        #=============== MATRIX X VALUE =================

        x = []          # Initialize matrix

        print("Enter the Row wise Entries:")

        for i in range(self.rows):         
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            x.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(x[i][j], end = " ")
            print()

        print("Matrix A = \n",x)

        x = np.array(x)
        A = np.array(A)

        #=================== GET ALPHA VALUES ====================

        x_transpose = x.transpose()

        print("Original Matrix x= \n",x)
        print("Transpose Matrix x= \n",x_transpose)
        print("The value A = \n", A)

        outputt = self.alpha*x*x_transpose+A

        print("------------- OUTPUT ---------------")
        print(outputt)

# -----------------------------------------------------------------------------------------------------------------------------

    def symmetric_rank1_operation(self):
        print("------------------------------------------")
        print("SYMMETRIC RANK 1 OPERATION")
        print("------------------------------------------")

        # === VALUE OF A ======       

        A = []              # Initialize matrix

        print("Enter the Rows:")

        for i in range(self.rows):         
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            A.append(a) 

        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end = " ")
            print()

        print("Matrix A = \n",A)

        def symmetric(row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if(i < j or i >j):
                        A[i][j] = A[j][i]
                
        print("Symmetric Matrix: ")
        symmetric(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end=" ")
            print()
        print("Matrix A = \n",A)

        #==== MATRIX X VALUE ======
        
        x = []          # Initialize matrix

        print("Enter the Row wise Entries:")

        for i in range(self.rows):         
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            x.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(x[i][j], end = " ")
            print()

        print("Matrix A = \n",x)

        x = np.array(x)
        A = np.array(A)

        #=============== GET ALPHA VALUES ==============

        alpha_val = int(input("Enter the Alpha value :"))

        x_transpose = x.transpose()

        print("Original Matrix x= \n",x)
        print("Transpose Matrix x= \n",x_transpose)
        print("The value A = \n", A)

        outputt = self.alpha*x*x_transpose+A

        print("------------- OUTPUT ---------------")
        print(outputt)

# -----------------------------------------------------------------------------------------------------------------------------

    def symmetric_rank2_operation(self):
        print("------------------------------------------")
        print("SYMMETRIC  RANK 2 OPERATION")
        print("------------------------------------------")

        #[1, 2, 0],[2, 2, 0],[0, 0, 0]

        # =============== VALUE OF A ================

        A = []          # Initialize matrix

        print("Enter the Rows:")

        for i in range(self.rows):         
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            A.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end = " ")
            print()

        print("Matrix A = \n",A)

        def symmetric(row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if(i < j or i >j):
                        A[i][j] = A[j][i]
                
        print("Symmetric Matrix: ")
        symmetric(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end=" ")
            print()
        print("Matrix A = \n",A)

        #================= MATRIX X VALUE ===================

        x = []          # Initialize matrix

        print("Enter the Row wise Entries:")

        for i in range(self.rows):         
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            x.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(x[i][j], end = " ")
            print()

        print("Matrix A = \n",x)

        x = np.array(x)
        A = np.array(A)

        #============= GET ALPHA VALUES ============

        x_transpose = x.transpose()

        print("Original Matrix x= \n",x)
        print("Transpose Matrix x= \n",x_transpose)
        print("The value A = \n", A)

        outputt=self.alpha*x*x_transpose + self.alpha*x_transpose*x + A

        print("------------- OUTPUT ---------------")
        print(outputt)

# -----------------------------------------------------------------------------------------------------------------------------

    # print(" FOR DOUBLE ")
    # print("MATRIX VECTOR MULTIPLY")


    def matrix_vector_double(self):
        # For Matrix A

        matrix_a = []  # Initialize matrix

        print("Enter the Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            matrix_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_a[i][j], end=" ")
            print()

        print("Matrix A = \n", matrix_a)

        #  For matrix B

        matrix_b = []   # Initialize matrix
        print("Enter the entries rowwise:")

        for i in range(no_of_rows1):  # For user input A for loop for row entries
            a = []
            for j in range(no_of_col1):  # A for loop for column entries
                a.append(int(input()))
            matrix_b.append(a)

        for i in range(no_of_rows1):  # For printing the matrix
            for j in range(no_of_col1):
                print(matrix_b[i][j], end=" ")
            print()

        print("Matrix B = \n", matrix_b)

        vector_size = int(input("enter size of vector: "))

        vector=[]
        print("enter entries ")
        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res_1 = np.dot(matrix_a,vector)
        final_res_2 = np.dot(matrix_b,vector)

        print(" --------- Matrix multiplication: ------------ ")
        print("The Result")
        print(final_res_1)
        print(final_res_2)

# -----------------------------------------------------------------------------------------------------------------------------

    def symmetric_matrix_vector_double(self):
        print("SYMMETRIC MATRIX VECTOR MULTIPLY")
        matrix_sym_a = []

        print("Enter the Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n", matrix_sym_a)

        def symmetric(row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if(i < j or i >j):
                        matrix_sym_a[i][j] = matrix_sym_a[j][i]
                
        print("Symmetric Matrix: ")
        symmetric(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n",matrix_sym_a)

        matrix_sym_b = []

        print("Enter the Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            matrix_sym_b.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_b[i][j], end=" ")
            print()

        print("Matrix A = \n", matrix_sym_b)

        def symmetric(row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if(i < j or i >j):
                        matrix_sym_b[i][j] = matrix_sym_b[j][i]
                
        print("Symmetric Matrix: ")
        symmetric(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_b[i][j], end=" ")
            print()
        print("Matrix A = \n",matrix_sym_b)

        vector_size = int(input("enter size of vector: "))

        vector=[]
        print("enter entries ")
        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res_1 = np.dot(matrix_sym_a,vector)
        final_res_2 = np.dot(matrix_sym_b,vector)

        print("Matrix multiplication: ")
        print("The Result")
        print(final_res_1, "\n")
        print(final_res_2, "\n")

# -----------------------------------------------------------------------------------------------------------------------------

    def triangular_matrix_vector_double(self):
        print("TRAINGULAR MATRIX VECTOR MULTIPLY")

        matrix_sym_a = []

        print("Enter the Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n", matrix_sym_a)

        def lower_a(matrix, row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if (i < j):
                        print("0", end=" ")
                    else:
                        print(matrix[i][j],end=" ")
                print(" ")
                
        matrix_sym_b = []

        print("Enter the Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            matrix_sym_b.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_b[i][j], end=" ")
            print()
        print("Matrix B = \n", matrix_sym_b)

        def lower_b(matrix, row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if (i < j):
                        print("0", end=" ")
                    else:
                        print(matrix[i][j],end=" ")
                print(" ")
                
        print("Triangular matrix: ")
        lower_a(matrix_sym_a, self.rows, self.cols)
        print(matrix_sym_a,"\n")
        lower_b(matrix_sym_b, self.rows, self.cols)
        print(matrix_sym_b,"\n")

        vector_size = int(input("enter size of vector: "))

        vector = []
        print("enter entries ")
        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res_1 = np.dot(matrix_sym_a,vector)
        final_res_2 = np.dot(matrix_sym_b,vector)

        print("Matrix multiplication: ")
        print("The Result")
        print(final_res_1, "\n")
        print(final_res_2, "\n")

# -----------------------------------------------------------------------------------------------------------------------------

    def triangular_banded_matrix_vector_double(self):
        print("TRIANGULAR BANDED MATRIX MULTIPLICATION")

        # ============= MATRIX A ==============

        matrix_sym_a = []

        print("Enter the Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n", matrix_sym_a)

        matrix_sym_b = []

        print("Enter the Entries:")

        for i in range(no_of_rows_b):
            a = []
            for j in range(no_of_col_b):
                a.append(int(input()))
            matrix_sym_b.append(a)

        for i in range(no_of_rows_b):
            for j in range(no_of_col_b):
                print(matrix_sym_b[i][j], end=" ")
            print()
        print("Matrix B = \n", matrix_sym_b)

        k = 1
        def lower_a(matrix, row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if (i < j):
                        print("0", end=" ")
                        matrix_sym_a[i][j] = (0)
                    else:
                        print(matrix[i][j],end=" ")
                        matrix_sym_a[i][j] = matrix[i][j]
                        
                        if i-j>k:
                            matrix_sym_a[i][j] = 0
                print(" ")

        def upper_b(matrix, row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if (i > j):
                        print("0", end=" ")
                        matrix_sym_b[i][j] = (0)
                    else:
                        print(matrix[i][j],end=" ")
                        matrix_sym_b[i][j] = matrix[i][j]
                        
                        if j-i>k:
                            matrix_sym_b[i][j] = 0
                print(" ")

        print("Triangular matrix: ")
        lower_a(matrix_sym_a, self.rows, self.cols)
        print(matrix_sym_a,"\n")
        upper_b(matrix_sym_b, no_of_rows_b, no_of_col_b)
        print(matrix_sym_b,"\n")

        vector_size = int(input("enter size of vector: "))
        
        vector=[]
        print("enter entries vector entries: ")

        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res_a = np.dot(matrix_sym_a, vector)
        final_res_b = np.dot(matrix_sym_b, vector)

        print("The Result: ")
        print(final_res_a)
        print(final_res_b)

# -----------------------------------------------------------------------------------------------------------------------------

    def Rank_1_operation_double(self):
        print("RANK 1 OPERATION")
        
        #  VALUE OF A

        A = []      # Initialize matrix
        print("Enter the Row wise Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            A.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end=" ")
            print()
        print("Matrix A = \n", A)

        # ================ MATRIX X VALUE ====================

        x = [] # Initialize matrix

        print("Enter the Row wise Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            x.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(x[i][j], end=" ")
            print()

        print("Matrix A = \n", x)

        # ================ MATRIX Y VALUE =====================

        y = []      # Initialize matrix
        print("Enter the Row wise Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            y.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(y[i][j], end=" ")
            print()

        print("Matrix Y = \n", y)

        x = np.array(x)
        y = np.array(y)
        A = np.array(A)

        # =================== GET ALPHA VALUES =====================

        x_transpose = x.transpose()
        y_transpose = y.transpose()

        print("Original Matrix x= \n", x)
        print("Transpose Matrix x= \n", x_transpose)
        print("Original Matrix y= \n", y)
        print("Transpose Matrix y= \n", y_transpose)

        print("The value A = \n", A)

        outputt = self.alpha * x * y_transpose + A

        print("------------- OUTPUT ---------------")
        print(outputt,"\n")

# -----------------------------------------------------------------------------------------------------------------------------

    def symmetric_rank1_operation_double(self):
        rint("SYMMETRIC RANK 1 OPERATION")

        # ==================== VALUE OF A =====================

        A = []      # Initialize matrix

        print("Enter the Rows:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            A.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end=" ")
            print()

        print("Matrix A = \n", A)

        def symmetric(row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if(i < j or i >j):
                        A[i][j] = A[j][i]
                
        print("Symmetric Matrix: ")
        symmetric(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end=" ")
            print()
        print("Matrix A = \n",A)

        # ============= MATRIX X VALUE ==================

        x = []  # Initialize matrix

        print("Enter the Row wise Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            x.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(x[i][j], end=" ")
            print()

        print("Matrix X = \n", x)

        # ====================== MATRIX Y VALUE =======================

        y = []  # Initialize matrix

        print("Enter the Row wise Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            y.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(y[i][j], end=" ")
            print()

        print("Matrix Y = \n", y)

        x = np.array(x)
        y = np.array(y)
        A = np.array(A)

        # == GET ALPHA VALUES ===

        x_transpose = x.transpose()
        y_transpose = y.transpose()

        print("Original Matrix x= \n", x)
        print("Transpose Matrix x= \n", x_transpose)
        print("Original Matrix y= \n", x)
        print("Transpose Matrix y= \n", x_transpose)
        print("The value A = \n", A)

        outputt = self.alpha * x * y_transpose + A

        print("------------- OUTPUT ---------------")
        print(outputt,"\n")

# -----------------------------------------------------------------------------------------------------------------------------

    def symmetric_rank2_operation_double(self):
        print("SYMMETRIC  RANK 2 OPERATION")
        # ==================== VALUE OF A ====================

        A = [] # Initialize matrix

        print("Enter the Rows:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            A.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end=" ")
            print()
        print("Matrix A = \n", A)

        def symmetric(row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if(i < j or i >j):
                        A[i][j] = A[j][i]
                
        print("Symmetric Matrix: ")
        symmetric(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                print(A[i][j], end=" ")
            print()
        print("Matrix A = \n",A)

        # =============== MATRIX X VALUE ===================

        x = []  # Initialize matrix

        print("Enter the Row wise Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            x.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(x[i][j], end=" ")
            print()
        print("Matrix A = \n", x)

        # ================ MATRIX Y VALUE ===================

        y = [] # Initialize matrix

        print("Enter the Row wise Entries:")

        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(int(input()))
            y.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(y[i][j], end=" ")
            print()

        print("Matrix X = \n", y)

        x = np.array(x)
        y = np.array(y)
        A = np.array(A)

        # =============== GET ALPHA VALUES ================

        x_transpose = x.transpose()
        y_transpose = y.transpose()

        print("Original Matrix x=\n", x)
        print("Transpose Matrix x=\n", x_transpose)
        print("Original Matrix y=\n", y)
        print("Transpose Matrix y=\n", y_transpose)
        print("The value A =\n", A)

        outputt = self.alpha * x * y_transpose + self.alpha * y * x_transpose + A

        print("------------- OUTPUT ---------------")
        print(outputt,"\n")

# -----------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------ INPUT ------------------------------------------------------
# rows = int(input("Enter the number of rows:"))
# cols = int(input("Enter the number of columns:"))
# alpha = int(input("Enter the value of alpha:"))
# A = int(input("Enter the value of A:"))

# single = BLAS_2(rows, cols, alpha, A)