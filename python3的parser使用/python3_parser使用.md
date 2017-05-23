# html.parser-简单的HTML和XHTML解析器 #

该模块定义了一个类HTMLParser，用做解析以HTML(超文本标记语言)和XHTML格式化的文本文件的基础

## 函数定义 ##
	
	class html.parser.HTMLParser(*,convert_charrefs =True)

	创建一个能够解析无效标记的解析器实例。
	
	如果convert_charrefs是True（默认值），则所有字符引用（除script/ style元素中的除外）都将自动转换为相应的Unicode字符。
	
	HTMLParser当遇到开始标签，结束标签，文本，注释和其他标记元素时，一个实例被提供HTML数据并调用处理程序方法。用户应该子类化HTMLParser并覆盖其方法来实现所需的行为。
	
	此解析器不会检查结束标记与起始标记的匹配，或者通过关闭外部元素来隐式关闭的元素调用结束标记处理程序。
	
	在版本3.4中更改：convert_charrefs关键字参数已添加。
	
	改变在3.5版本中：对于参数的默认值convert_charrefs现在True。

例子一：

	from html.parser import HTMLParser
	
	class MyHTMLParser(HTMLParser):
	    def handle_starttag(self, tag, attrs):
	        print("Encountered a start tag:", tag)
	
	    def handle_endtag(self, tag):
	        print("Encountered an end tag :", tag)
	
	    def handle_data(self, data):
	        print("Encountered some data  :", data)
	
	parser = MyHTMLParser()
	parser.feed('<html><head><title>Test</title></head>'
	            '<body><h1>Parse me!</h1></body></html>')


输出结果：

	Encountered a start tag: html
	Encountered a start tag: head
	Encountered a start tag: title
	Encountered some data  : Test
	Encountered an end tag : title
	Encountered an end tag : head
	Encountered a start tag: body
	Encountered a start tag: h1
	Encountered some data  : Parse me!
	Encountered an end tag : h1
	Encountered an end tag : body
	Encountered an end tag : html
	>>> 

它使用 HTMLParser类来打印出遇到的开始标签，结束标签和数据：

## HTMLParser方法 ##

	HTMLParser.feed(data)
	给解析器提供一些文本

	HTMLParser.close() 
	对缓冲区数据强制处理关闭

	HTMLParser.reset()
	重置实例

	HTMLParser.getpos()
	返回当前行号和偏移量
	
	HTMLParser.get_starttag_text()
	返回最近打开的开始标签的文本。
	
	HTMLParser.handle_starttag(tag, attrs)
	这个方法被调用来处理标签的开始 例如 <div id="main">

	HTMLParser.handle_endtag(tag)
	这个方法被调用来处理元素的结束标签（例如</div>）

	HTMLParser.handle_startendtag(tag, attrs)
	HTMLParser.handle_data(data)
	HTMLParser.handle_entityref(name)
	HTMLParser.handle_charref(name)
	HTMLParser.handle_comment(data)
	HTMLParser.handle_decl(decl)
	HTMLParser.handle_pi(data)
	HTMLParser.unknown_decl(data)


例子二：

下面编码实现了一个解析器

	from html.parser import HTMLParser
	from html.entities import name2codepoint
	
	class MyHTMLParser(HTMLParser):
	    def handle_starttag(self, tag, attrs):
	        print("Start tag:", tag)
	        for attr in attrs:
	            print("     attr:", attr)
	
	    def handle_endtag(self, tag):
	        print("End tag  :", tag)
	
	    def handle_data(self, data):
	        print("Data     :", data)
	
	    def handle_comment(self, data):
	        print("Comment  :", data)
	
	    def handle_entityref(self, name):
	        c = chr(name2codepoint[name])
	        print("Named ent:", c)
	
	    def handle_charref(self, name):
	        if name.startswith('x'):
	            c = chr(int(name[1:], 16))
	        else:
	            c = chr(int(name))
	        print("Num ent  :", c)
	
	    def handle_decl(self, data):
	        print("Decl     :", data)
	
	parser = MyHTMLParser()

解析一个文本

	>>> parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '+'"http://www.w3.org/TR/html4/strict.dtd">')
	Decl     : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"

解析一个带属性和标题的元素：

	>>> parser.feed('<img src="python-logo.png" alt="The Python logo">')
	Start tag: img
	     attr: ('src', 'python-logo.png')
	     attr: ('alt', 'The Python logo')
	>>> 

	>>> parser.feed('<h1>Python</h1>')
	Start tag: h1
	Data     : Python
	End tag  : h1
	>>>

内容script和style元素按原样返回，无需进一步解析 

	>>> parser.feed('<style type="text/css">#python { color: green }</style>')
	Start tag: style
	     attr: ('type', 'text/css')
	Data     : #python { color: green }
	End tag  : style
	>>> 

	>>> parser.feed('<script type="text/javascript">' + 'alert("<strong>hello!</strong>");</script>')
	Start tag: script
	     attr: ('type', 'text/javascript')
	Data     : alert("<strong>hello!</strong>");
	End tag  : script
	>>> 

解析注释

	>>> parser.feed('<!-- a comment -->' +  '<!--[if IE 9]>IE-specific content<![endif]-->')
	Comment  :  a comment 
	Comment  : [if IE 9]>IE-specific content<![endif]
	>>> 