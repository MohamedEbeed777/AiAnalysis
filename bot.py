import pandas as pd
import numpy as np

print("=== Data Analysis Program using Python + Pandas + NumPy ===\n")

# Ask user to upload Excel file
file_path = input("Enter Excel file path: ")

# Read the file
try:
    df = pd.read_excel(file_path)
    print("\n✔ File loaded successfully!\n")
except:
    print("❌ Error loading file. Please check the path.")
    exit()

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Operations list
operations = {
    "1": "Sum",
    "2": "Transpose",
    "3": "Sort",
    "4": "Set Index",
    "5": "GroupBy",
    "6": "Describe",
    "7": "Mean",
    "8": "Median",
    "9": "Unique Values",
    "10": "Convert to NumPy Array",
    "11": "Show Shape",
    "12": "Drop row using iloc",
    "13": "Drop row containing a value using loc",
    "14": "Replace values in a column using np.where",
    "15": "Exit",
    "16": "Stack",
    "17": "Unstack",
    "18": "Pivot",
    "19": "Advanced Math Operations",
    "20": "One-Hot Encoding & Merge",
    "21": "Column Management (Drop / DropNa / FillNa / IsNull / NotNull)"
}

# Function for Preview or Apply
def apply_or_preview(df, func, *args, **kwargs):
    print("\nDo you want to apply this operation to the DataFrame or just preview?")
    print("1 - Preview")
    print("2 - Apply")
    choice = input("Your choice: ")
    if choice == "1":
        print("\n=== Preview ===")
        func(*args, **kwargs)
        return df
    elif choice == "2":
        print("\n=== Apply ===")
        df = func(*args, **kwargs)
        return df
    else:
        print("❌ Invalid choice! Preview will be shown by default.")
        func(*args, **kwargs)
        return df

# Main program loop
while True:
    print("\n=== Select an operation ===")
    for key, val in operations.items():
        print(f"{key} - {val}")

    choice = input("\nYour choice: ")

    # 1- SUM
    if choice == "1":
        def sum_func(df):
            print(df.select_dtypes(include=[np.number]).sum())
            return df
        df = apply_or_preview(df, sum_func, df)

    # 2- Transpose
    elif choice == "2":
        def transpose_func(df):
            print(df.T)
            return df
        df = apply_or_preview(df, transpose_func, df)

    # 3- Sort
    elif choice == "3":
        print("\nAvailable columns:")
        for i, c in enumerate(df.columns):
            print(f"{i+1} - {c}")
        idx = int(input("Choose column number to sort: "))
        col = df.columns[idx-1]
        order = input("Ascending? (y/n): ").lower()
        asc = True if order == "y" else False

        def sort_func(df):
            df_sorted = df.sort_values(by=col, ascending=asc)
            print(df_sorted)
            return df_sorted

        df = apply_or_preview(df, sort_func, df)

    # 4- Set Index
    elif choice == "4":
        for i, c in enumerate(df.columns):
            print(f"{i+1} - {c}")
        idx = int(input("Choose column number for index: "))
        col = df.columns[idx-1]

        def setindex_func(df):
            df_new = df.set_index(col)
            print(df_new.head())
            return df_new

        df = apply_or_preview(df, setindex_func, df)

    # 5- GroupBy
    elif choice == "5":
        for i, c in enumerate(df.columns):
            print(f"{i+1} - {c}")
        idx = int(input("Choose column number for GroupBy: "))
        col = df.columns[idx-1]

        print("\nSelect GroupBy operation:")
        print("1 - sum")
        print("2 - mean")
        print("3 - count")
        g_choice = input("Your choice: ")

        def groupby_func(df):
            if g_choice == "1": print(df.groupby(col).sum())
            elif g_choice == "2": print(df.groupby(col).mean())
            elif g_choice == "3": print(df.groupby(col).count())
            else: print("❌ Invalid choice!")
            return df

        df = apply_or_preview(df, groupby_func, df)

    # 6- Describe
    elif choice == "6":
        def describe_func(df):
            print(df.describe())
            return df
        df = apply_or_preview(df, describe_func, df)

    # 7- Mean
    elif choice == "7":
        def mean_func(df):
            print(df.mean(numeric_only=True))
            return df
        df = apply_or_preview(df, mean_func, df)

    # 8- Median
    elif choice == "8":
        def median_func(df):
            print(df.median(numeric_only=True))
            return df
        df = apply_or_preview(df, median_func, df)

    # 9- Unique
    elif choice == "9":
        for i, c in enumerate(df.columns):
            print(f"{i+1} - {c}")
        idx = int(input("Choose column number to view unique values: "))
        col = df.columns[idx-1]

        def unique_func(df):
            print(df[col].unique())
            return df

        df = apply_or_preview(df, unique_func, df)

    # 10- Convert to NumPy Array
    elif choice == "10":
        def to_numpy_func(df):
            arr = df.to_numpy()
            print(arr)
            print("Shape:", arr.shape)
            return df
        df = apply_or_preview(df, to_numpy_func, df)

    # 11- Show Shape
    elif choice == "11":
        def shape_func(df):
            print("Data shape:", df.shape)
            return df
        df = apply_or_preview(df, shape_func, df)

    # 12- Drop row using iloc
    elif choice == "12":
        row = int(input("Enter row number to drop (starting 0): "))

        def drop_row_func(df):
            df_new = df.drop(df.index[row])
            print(df_new.head())
            return df_new

        df = apply_or_preview(df, drop_row_func, df)

    # 13- Drop row containing a value using loc
    elif choice == "13":
        for i, c in enumerate(df.columns):
            print(f"{i+1} - {c}")
        idx = int(input("Choose column number: "))
        col = df.columns[idx-1]
        value = input("Enter the value to delete rows containing it: ")

        def drop_value_func(df):
            df_new = df[df[col].astype(str) != value]
            print(df_new.head())
            return df_new

        df = apply_or_preview(df, drop_value_func, df)

    # 14- Replace values using np.where
    elif choice == "14":
        for i, c in enumerate(df.columns):
            print(f"{i+1} - {c}")
        idx = int(input("Choose column number to replace values: "))
        col = df.columns[idx-1]
        old_value = input("Old value: ")
        new_value = input("New value: ")

        def replace_func(df):
            df[col] = np.where(df[col].astype(str) == old_value, new_value, df[col])
            print(df.head())
            return df

        df = apply_or_preview(df, replace_func, df)

    # 15- Exit
    elif choice == "15":
        print("Program terminated 👋")
        break

    # 16- Stack
    elif choice == "16":
        def stack_func(df):
            print(df.stack())
            return df
        df = apply_or_preview(df, stack_func, df)

    # 17- Unstack
    elif choice == "17":
        def unstack_func(df):
            print(df.unstack())
            return df
        df = apply_or_preview(df, unstack_func, df)

    # 18- Pivot
    elif choice == "18":
        for i, c in enumerate(df.columns):
            print(f"{i+1} - {c}")
        idx_i = int(input("Choose index column number: "))
        idx_c = int(input("Choose columns column number: "))
        idx_v = int(input("Choose values column number: "))
        index_col = df.columns[idx_i-1]
        columns_col = df.columns[idx_c-1]
        value_col = df.columns[idx_v-1]

        def pivot_func(df):
            print(df.pivot(index=index_col, columns=columns_col, values=value_col))
            return df

        df = apply_or_preview(df, pivot_func, df)

    # 19- Advanced Math Operations
    elif choice == "19":
        numeric_cols = list(df.select_dtypes(include=[np.number]).columns)
        print("Numeric columns available:", numeric_cols)
        idx = int(input("Choose column number: "))
        col = numeric_cols[idx-1]

        print("1-sum 2-mean 3-max 4-min 5-diff 6-square 7-sqrt 8-cumsum 9-cumprod 10-abs")
        print("11-log 12-log10 13-log2 14-power 15-cbrt 16-sin 17-cos 18-tan 19-exp 20-round 21-floor 22-ceil")
        op = input("Choose operation: ")

        def math_func(df):
            try:
                series = df[col]
                if op=="1": print(series.sum())
                elif op=="2": print(series.mean())
                elif op=="3": print(series.max())
                elif op=="4": print(series.min())
                elif op=="5": print(series.diff())
                elif op=="6": print(series**2)
                elif op=="7": print(np.sqrt(series))
                elif op=="8": print(series.cumsum())
                elif op=="9": print(series.cumprod())
                elif op=="10": print(series.abs())
                elif op=="11": print(np.log(series))
                elif op=="12": print(np.log10(series))
                elif op=="13": print(np.log2(series))
                elif op=="14":
                    val=float(input("Enter power value: "))
                    print(np.power(series,val))
                elif op=="15": print(np.cbrt(series))
                elif op=="16": print(np.sin(series))
                elif op=="17": print(np.cos(series))
                elif op=="18": print(np.tan(series))
                elif op=="19": print(np.exp(series))
                elif op=="20": print(series.round())
                elif op=="21": print(np.floor(series))
                elif op=="22": print(np.ceil(series))
                else: print("❌ Invalid choice!")
            except Exception as e:
                print("❌ Error:", e)
            return df

        df = apply_or_preview(df, math_func, df)

    # 20- One-Hot Encoding
    elif choice == "20":
        cat_cols = list(df.select_dtypes(include=['object']).columns)
        print("Categorical columns:", cat_cols)
        idx = int(input("Choose column number for One-Hot Encoding: "))
        col = cat_cols[idx-1]

        def onehot_func(df):
            dummies = pd.get_dummies(df[col], prefix=col)
            df_new = df.drop(columns=[col])
            df_new = pd.concat([df_new, dummies], axis=1)
            print(df_new.head())
            return df_new

        df = apply_or_preview(df, onehot_func, df)

    # 21- Column Management
    elif choice == "21":
        print("1- Drop column 2- Drop empty columns 3- Fill NaN 4- Check NaN")
        sub_choice = input("Your choice: ")

        def manage_cols_func(df):
            if sub_choice=="1":
                for i, c in enumerate(df.columns):
                    print(f"{i+1} - {c}")
                idx = int(input("Choose column number to drop: "))
                df = df.drop(columns=[df.columns[idx-1]])
                print(df.head())
            elif sub_choice=="2":
                df = df.dropna(axis=1)
                print(df.head())
            elif sub_choice=="3":
                val=input("Enter fill value: ")
                try: val=float(val)
                except: pass
                df = df.fillna(val)
                print(df.head())
            elif sub_choice=="4":
                print("isnull():\n", df.isnull())
                print("notnull():\n", df.notnull())
            else:
                print("❌ Invalid choice!")
            return df

        df = apply_or_preview(df, manage_cols_func, df)

    else:
        print("❌ Invalid choice!")