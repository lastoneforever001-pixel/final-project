<!DOCTYPE html>
<html>
<head>
    <title>MY FIRST WEBSITE </title>

</head>

<body>

    <h1> MY PYTHON WEDSITE </h1>
    <form method ="POST"
     <input type="text" name ="name"
placeholder name="Enter your name">
    <bottpn type="submit">Submit</button>
    </form>

{%if name %}
    <h2>Hello{{name}}!</h2>
    {%end%}