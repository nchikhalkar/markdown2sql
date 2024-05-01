from flask import Flask, request, render_template, redirect, url_for
import re

app = Flask(__name__)

def markdown_to_sql(markdown_input):
    # Extract column names and types from markdown input
    columns = re.findall(r'\| (\w+) \| (\w+) \|', markdown_input)
    
    # Generate SQL create table query
    table_name = "your_table_name"  # Replace with desired table name
    create_table_query = f"CREATE TABLE {table_name} (\n"
    
    for column in columns[1:]:  # Skip the first row with headers
        create_table_query += f"    {column[0]} {column[1]},\n"
    
    create_table_query = create_table_query.rstrip(',\n') + "\n);"
    
    return create_table_query

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        markdown_input = request.form['markdown_input']
        sql_output = markdown_to_sql(markdown_input)
        return render_template('result.html', sql_output=sql_output)

    return render_template('index.html', markdown_input=None, sql_output=None)

if __name__ == '__main__':
    app.run(debug=True)
