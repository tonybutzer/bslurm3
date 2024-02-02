import pandas as pd
import plotly.figure_factory as ff

# Create a sample DataFrame
data = {'Task': ['Task 1', 'Task 2', 'Milestone 1'],
        'Start': ['2023-11-05 08:00:00', '2023-11-05 09:00:00', '2023-11-05 10:00:00'],
        'Finish': ['2023-11-05 10:00:00', '2023-11-05 12:00:00', '2023-11-05 10:30:00']}

df = pd.DataFrame(data)
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

# Create the Gantt chart figure
fig = ff.create_gantt(df, colors=['#7a7a7a', '#5A9BD5', '#A9D18E'], index_col='Task',
                       show_colorbar=True, group_tasks=True)

# Update layout
fig.update_layout(title='Gantt Chart Example',
                  xaxis_title='Timeline',
                  yaxis_title='Tasks',
                  yaxis_categoryorder='total ascending')

# Show the figure
fig.show()


