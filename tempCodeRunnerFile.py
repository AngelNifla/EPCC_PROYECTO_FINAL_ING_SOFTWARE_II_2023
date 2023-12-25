@app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         _email = request.form['typeEmailX']
#         _password = request.form['typePasswordX']
#         cursor = mysql.connection.cursor()
#         cursor.execute("Use tif")
#         cursor.execute("SELECT * FROM Usuario WHERE correo = %s AND nombre = %s", (_email, _password))
#         data = cursor.fetchall()
#         if len(data) > 0:
#             session['user'] = _email
#             return redirect(url_for('home'))
#         cursor.close()
#         flash('Contraseña o usuario incorrecto')
#         return redirect('login')

