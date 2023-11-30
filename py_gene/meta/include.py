

def mark():
  doctype=  '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
{body}
<script src=""></script> 
</body>
</html>

'''.format( title = "hello html", body = "hello html!" ) 
  return  doctype
  

if __name__ == '__main__':
    print(__name__)
  