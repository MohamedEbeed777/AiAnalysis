import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Interactive Excel Data Processor (Python + Pandas + NumPy)")

# ⿡ Upload Excel File
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("File loaded successfully!")
        st.dataframe(df.head())
    except:
        st.error("Error reading the Excel file!")
        st.stop()
else:
    st.info("Please upload a file to continue.")
    st.stop()

# ⿢ Select Operation
operation = st.selectbox(
    "Select an operation",
    [
        "Sum", "Transpose", "Sort", "Set Index", "GroupBy",
        "Describe", "Mean", "Median", "Unique Values",
        "Convert to NumPy Array", "Show Shape",
        "Drop row using iloc", "Drop row containing a value using loc",
        "Replace values using np.where", "Stack", "Unstack", "Pivot",
        "Advanced Math Operations", "One-Hot Encoding",
        "Column Management"
    ]
)

# Helper function to select a column
def select_column(df, prompt="Select a column"):
    col = st.selectbox(prompt, df.columns)
    return col

# Operations
if operation == "Sum":
    st.write(df.select_dtypes(include=[np.number]).sum())

elif operation == "Transpose":
    st.dataframe(df.T)

elif operation == "Sort":
    col = select_column(df, "Select column to sort")
    asc = st.radio("Ascending?", ["Yes", "No"]) == "Yes"
    df_sorted = df.sort_values(by=col, ascending=asc)
    st.dataframe(df_sorted)

elif operation == "Set Index":
    col = select_column(df, "Select column for index")
    df_indexed = df.set_index(col)
    st.dataframe(df_indexed)

elif operation == "GroupBy":
    col = select_column(df, "Select column for GroupBy")
    func = st.selectbox("Select aggregation", ["sum", "mean", "count"])
    if func == "sum":
        st.dataframe(df.groupby(col).sum())
    elif func == "mean":
        st.dataframe(df.groupby(col).mean())
    else:
        st.dataframe(df.groupby(col).count())

elif operation == "Describe":
    st.dataframe(df.describe())

elif operation == "Mean":
    st.write(df.mean(numeric_only=True))

elif operation == "Median":
    st.write(df.median(numeric_only=True))

elif operation == "Unique Values":
    col = select_column(df)
    st.write(df[col].unique())

elif operation == "Convert to NumPy Array":
    st.write(df.to_numpy())
    st.write("Shape:", df.to_numpy().shape)

elif operation == "Show Shape":
    st.write("Shape:", df.shape)

elif operation == "Drop row using iloc":
    row = st.number_input("Enter row number (starting from 0)", min_value=0, max_value=len(df)-1, step=1)
    df_dropped = df.drop(df.index[row])
    st.dataframe(df_dropped)

elif operation == "Drop row containing a value using loc":
    col = select_column(df)
    val = st.text_input("Enter value to remove rows containing it")
    if val:
        df_filtered = df[df[col].astype(str) != val]
        st.dataframe(df_filtered)

elif operation == "Replace values using np.where":
    col = select_column(df)
    old_val = st.text_input("Old value")
    new_val = st.text_input("New value")
    if old_val and new_val:
        df[col] = np.where(df[col].astype(str) == old_val, new_val, df[col])
        st.dataframe(df)

elif operation == "Stack":
    st.dataframe(df.stack())

elif operation == "Unstack":
    st.dataframe(df.unstack())

elif operation == "Pivot":
    index_col = select_column(df, "Select index column")
    columns_col = select_column(df, "Select columns column")
    values_col = select_column(df, "Select values column")
    st.dataframe(df.pivot(index=index_col, columns=columns_col, values=values_col))

elif operation == "Advanced Math Operations":
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    col = select_column(df, "Select numeric column")
    op = st.selectbox(
        "Select operation",
        ["sum","mean","max","min","diff","square","sqrt","cumsum","cumprod",
         "abs","log","log10","log2","power","cbrt","sin","cos","tan",
         "exp","round","floor","ceil"]
    )
    series = df[col]
    result = None
    try:
        if op=="sum": result = series.sum()
        elif op=="mean": result = series.mean()
        elif op=="max": result = series.max()
        elif op=="min": result = series.min()
        elif op=="diff": result = series.diff()
        elif op=="square": result = series**2
        elif op=="sqrt": result = np.sqrt(series)
        elif op=="cumsum": result = series.cumsum()
        elif op=="cumprod": result = series.cumprod()
        elif op=="abs": result = series.abs()
        elif op=="log": result = np.log(series)
        elif op=="log10": result = np.log10(series)
        elif op=="log2": result = np.log2(series)
        elif op=="power":
            val = st.number_input("Enter power value", value=2)
            result = np.power(series, val)
        elif op=="cbrt": result = np.cbrt(series)
        elif op=="sin": result = np.sin(series)
        elif op=="cos": result = np.cos(series)
        elif op=="tan": result = np.tan(series)
        elif op=="exp": result = np.exp(series)
        elif op=="round": result = series.round()
        elif op=="floor": result = np.floor(series)
        elif op=="ceil": result = np.ceil(series)
    except Exception as e:
        st.error(f"Error: {e}")
    if result is not None:
        st.dataframe(result)

elif operation == "One-Hot Encoding":
    cat_cols = df.select_dtypes(include=['object']).columns
    col = select_column(df, "Select categorical column")
    dummies = pd.get_dummies(df[col], prefix=col)
    df_new = pd.concat([df.drop(columns=[col]), dummies], axis=1)
    st.dataframe(df_new)

elif operation == "Column Management":
    action = st.selectbox("Select action", ["Drop Column","Drop Empty Columns","Fill NaN","Check NaN"])
    if action=="Drop Column":
        col = select_column(df, "Select column to drop")
        df_new = df.drop(columns=[col])
        st.dataframe(df_new)
    elif action=="Drop Empty Columns":
        df_new = df.dropna(axis=1)
        st.dataframe(df_new)
    elif action=="Fill NaN":
        val = st.text_input("Enter fill value")
        if val:
            try: val = float(val)
            except: pass
            df_new = df.fillna(val)
            st.dataframe(df_new)
    elif action=="Check NaN":
        st.write("isnull():")
        st.dataframe(df.isnull())
        st.write("notnull():")
        st.dataframe(df.notnull())
