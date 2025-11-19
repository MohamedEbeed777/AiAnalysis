import streamlit as st
import pandas as pd
import numpy as np

st.title("Synthra Ai 📊 Advanced Excel Data Processor (Python + Pandas + NumPy)")
facebook_page = "https://www.facebook.com/share/1Bvfup6DWi/"

st.write(f"[Contact us to join Python & Data Analysis course ]({facebook_page})")
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
        "Sum", "Mean", "Median", "Variance", "Std Dev", "Skew", "Kurtosis", "Correlation",
        "Transpose", "Sort", "Set Index", "GroupBy", "Describe",
        "Unique Values", "Convert to NumPy Array", "Show Shape",
        "Drop row using iloc", "Drop row containing a value using loc",
        "Replace values using np.where", "Remove Duplicates", "Filter Rows",
        "Text Operations", "Stack", "Unstack", "Pivot", "Advanced Math Operations",
        "One-Hot Encoding", "Column Management", "Top/Bottom N Rows"
    ]
)

def select_column(df, prompt="Select a column"):
    col = st.selectbox(prompt, df.columns)
    return col

def numeric_columns(df):
    return df.select_dtypes(include=[np.number]).columns

def categorical_columns(df):
    return df.select_dtypes(include=['object']).columns

# ⿣ Operations
if operation == "Sum":
    st.write(df[numeric_columns(df)].sum())

elif operation == "Mean":
    st.write(df[numeric_columns(df)].mean())

elif operation == "Median":
    st.write(df[numeric_columns(df)].median())

elif operation == "Variance":
    st.write(df[numeric_columns(df)].var())

elif operation == "Std Dev":
    st.write(df[numeric_columns(df)].std())

elif operation == "Skew":
    st.write(df[numeric_columns(df)].skew())

elif operation == "Kurtosis":
    st.write(df[numeric_columns(df)].kurt())

elif operation == "Correlation":
    st.write(df[numeric_columns(df)].corr())

elif operation == "Transpose":
    st.dataframe(df.T)

elif operation == "Sort":
    col = select_column(df, "Select column to sort")
    asc = st.radio("Ascending?", ["Yes", "No"]) == "Yes"
    st.dataframe(df.sort_values(by=col, ascending=asc))

elif operation == "Set Index":
    col = select_column(df, "Select column for index")
    st.dataframe(df.set_index(col))

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

elif operation == "Unique Values":
    col = select_column(df)
    st.write(df[col].unique())

elif operation == "Convert to NumPy Array":
    arr = df.to_numpy()
    st.write(arr)
    st.write("Shape:", arr.shape)

elif operation == "Show Shape":
    st.write("Shape:", df.shape)

elif operation == "Drop row using iloc":
    row = st.number_input("Enter row number (starting from 0)", min_value=0, max_value=len(df)-1, step=1)
    st.dataframe(df.drop(df.index[row]))

elif operation == "Drop row containing a value using loc":
    col = select_column(df)
    val = st.text_input("Enter value to remove rows containing it")
    if val:
        st.dataframe(df[df[col].astype(str) != val])

elif operation == "Replace values using np.where":
    col = select_column(df)
    old_val = st.text_input("Old value")
    new_val = st.text_input("New value")
    if old_val and new_val:
        df[col] = np.where(df[col].astype(str) == old_val, new_val, df[col])
        st.dataframe(df)

elif operation == "Remove Duplicates":
    st.dataframe(df.drop_duplicates())

elif operation == "Filter Rows":
    col = select_column(df)
    cond = st.text_input("Enter condition (example: '>5', '==\"IT\"')")
    if cond:
        st.dataframe(df.query(f"{col} {cond}"))

elif operation == "Text Operations":
    col = select_column(df)
    op = st.selectbox("Select text operation", ["Lower", "Upper", "Title", "Strip", "Replace"])
    if op == "Lower":
        st.dataframe(df[col].str.lower())
    elif op == "Upper":
        st.dataframe(df[col].str.upper())
    elif op == "Title":
        st.dataframe(df[col].str.title())
    elif op == "Strip":
        st.dataframe(df[col].str.strip())
    elif op == "Replace":
        old_val = st.text_input("Old substring")
        new_val = st.text_input("New substring")
        if old_val and new_val:
            st.dataframe(df[col].str.replace(old_val, new_val, regex=False))

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
    col = select_column(df, "Select numeric column")
    op = st.selectbox(
        "Select operation",
        ["sum","mean","max","min","diff","square","sqrt","cumsum","cumprod",
         "cummax","cummin","abs","log","log10","log2","power","cbrt","sin","cos","tan",
         "exp","round","floor","ceil","normalize","standardize"]
    )
    series = df[col]
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
        elif op=="cummax": result = series.cummax()
        elif op=="cummin": result = series.cummin()
        elif op=="abs": result = series.abs()
        elif op=="log": result = np.log(series)
        elif op=="log10": result = np.log10(series)
        elif op=="log2": result = np.log2(series)
        elif op=="power":
            val = st.number_input("Enter power value", value=2)
            result = np.power(series,val)
        elif op=="cbrt": result = np.cbrt(series)
        elif op=="sin": result = np.sin(series)
        elif op=="cos": result = np.cos(series)
        elif op=="tan": result = np.tan(series)
        elif op=="exp": result = np.exp(series)
        elif op=="round": result = series.round()
        elif op=="floor": result = np.floor(series)
        elif op=="ceil": result = np.ceil(series)
        elif op=="normalize":
            result = (series - series.min()) / (series.max() - series.min())
        elif op=="standardize":
            result = (series - series.mean()) / series.std()
        st.dataframe(result)
    except Exception as e:
        st.error(f"Error: {e}")

elif operation == "One-Hot Encoding":
    col = select_column(df, "Select categorical column")
    dummies = pd.get_dummies(df[col], prefix=col)
    df_new = pd.concat([df.drop(columns=[col]), dummies], axis=1)
    st.dataframe(df_new)

elif operation == "Column Management":
    action = st.selectbox("Select action", ["Drop Column","Drop Empty Columns","Fill NaN","Check NaN","Rename Column","Reorder Columns","Add Calculated Column"])
    if action=="Drop Column":
        col = select_column(df, "Select column to drop")
        st.dataframe(df.drop(columns=[col]))
    elif action=="Drop Empty Columns":
        st.dataframe(df.dropna(axis=1))
    elif action=="Fill NaN":
        val = st.text_input("Enter fill value")
        if val:
            try: val=float(val)
            except: pass
            st.dataframe(df.fillna(val))
    elif action=="Check NaN":
        st.write("isnull():")
        st.dataframe(df.isnull())
        st.write("notnull():")
        st.dataframe(df.notnull())
    elif action=="Rename Column":
        col = select_column(df, "Select column to rename")
        new_name = st.text_input("Enter new column name")
        if new_name:
            st.dataframe(df.rename(columns={col:new_name}))
    elif action=="Reorder Columns":
        new_order = st.multiselect("Select columns order", df.columns, default=df.columns)
        st.dataframe(df[new_order])
    elif action=="Add Calculated Column":
        new_col = st.text_input("New column name")
        expr = st.text_input("Enter calculation using existing columns (example: df[\"Age\"]*2)")
        if new_col and expr:
            try:
                df[new_col] = eval(expr)
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error: {e}")

elif operation == "Top/Bottom N Rows":
    col = select_column(df, "Select column for ranking")
    N = st.number_input("Enter N value", min_value=1, value=5)
    choice = st.radio("Top or Bottom?", ["Top", "Bottom"])
    if choice=="Top":
        st.dataframe(df.nlargest(N,col))
    else:
        st.dataframe(df.nsmallest(N,col))

st.write(
    f"""
    <div style="background-color:#28a745; padding:12px; border-radius:10px; text-align:center;">
        <a href="{facebook_page}" style="color:white; font-size:20px; font-weight:bold;" target="_blank">
            تواصل معنا على فيسبوك
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
 






