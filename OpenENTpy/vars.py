#================================
#         OPEN-ENT.PY
#================================
# 2023 EletrixTime




LOGIN_PAGE = """
<!doctype html>
<!--

 -->

<html>
	<head>
		<title>Authentification</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<script type="text/javascript" src="/assets/js/entcore/ng-app.js?v=1700233559677" id="context"></script>
		<script type="text/javascript" src="/auth/public/dist/application.js?v=1700233559677"></script>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
        <script type="text/javascript">var notLoggedIn = true;</script>
	</head>
	<body class="login" ng-controller="LoginController"
		  ng-init='error = ""; callBack = ""; mainPage = ""'>
		<default-styles>
			<div class="absolute">
             <div ng-include="template.containers.main"></div>
            </div>
		</default-styles>
	</body>
</html>
"""
