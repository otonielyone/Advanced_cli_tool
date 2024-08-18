from flask import Blueprint, render_template, request 
from flask_login import login_required, current_user

ptools = Blueprint('ptools', __name__)

@ptools.route('/home', methods=['GET','POST'])
@login_required
def home():
   return render_template('home.html', user=current_user)
 
@ptools.route('/findrack', methods=['GET','POST'])
@login_required
def findrack():
   if request.method == 'POST':
      a = request.form.get('suite')
      b = request.form.get('cage')
      c = request.form.get('rack')
      strr = [a,b,c]
      if a == '' or b == '' or c == '': 
         var = ''
         flag = False
      else:
         flag = True
         var = ':'.join(strr)
         cmd = "infosb.dclist("+var+")['result'][1]['host_name']"
      if flag:
         content = 'sshoutput'        
         with open(content, 'r') as f:            
            return render_template('findrack2.html', user=current_user, cmd=cmd, var3=f.read())          
      else:
         return render_template('findrack2.html', user=current_user)          
   return render_template('findrack.html', user=current_user)
   
@ptools.route('/findrack2', methods=['GET','POST'])
@login_required
def findrack2():
   return render_template('findrack2.html', user=current_user)
   
@ptools.route('/quickscan', methods=['GET','POST'])
@login_required
def quickscan():
   return render_template('quickscan.html', user=current_user)

@ptools.route('/deepscan', methods=['GET','POST'])
@login_required
def deepscan():
   return render_template('deepscan.html', user=current_user)

@ptools.route('/sillytools', methods=['GET','POST'])
@login_required
def sillytools():
   return render_template('sillytools.html', user=current_user)

@ptools.route('/convertmac', methods=['GET','POST'])
@login_required
def convertmac():
   if request.method == 'POST':
      import re
      string = request.form.get('mac') 
      macs = string.split() #creates list without white spaces
      array = []   
      for h in macs:
         m = re.sub('[.:-]', '', h).lower()  # remove puncs/converts to lower case
         cleanmac = ':'.join(m[i:i+2] for i in range(0,12,2)) #adds punc ":"
         array.append(cleanmac)
      if len(array) == 0: 
         array = ''

      return render_template('convertoutput.html', user=current_user, mac=array)        
   return render_template('convertmac.html', user=current_user)
      
@ptools.route('/convertoutput')
@login_required
def convertoutput():
   return render_template('convertoutput.html', user=current_user)
   
@ptools.route('/test', methods=['GET','POST'])
@login_required
def test():
   return render_template('test.html', user=current_user)
