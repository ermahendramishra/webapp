from graphviz import Digraph

dot = Digraph(comment='Web Application Diagram')

dot.node('WebApp', 'Web Application')
dot.node('HAProxy', 'HAProxy Load Balancer')
dot.node('SecurityGroup', 'Security Group')
dot.node('ServiceAccount', 'Service Account')

dot.edge('HAProxy', 'WebApp', label='HTTP Requests')
dot.edge('HAProxy', 'SecurityGroup', label='Secure Communication')
dot.edge('WebApp', 'SecurityGroup', label='Secure Communication')
dot.edge('ServiceAccount', 'WebApp', label='Access Permissions')

dot.render('web_app_diagram', format='png', cleanup=True)

print("Diagram generated successfully.")
