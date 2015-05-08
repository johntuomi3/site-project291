% rebase('blog_layout.tpl', title=title, year=year)
<div class="blog-container">
	<div class="overlay"></div>
	% if len(last_10) != 0:
	<div class = "blog-feed">	
		<ul>
		% for link in last_10:
		<li>{{ !link }} </li>
		% end
		</ul>
	</div>
	% end
	% if blog_content != None or blog_content != '':
	{{ !blog_content }}
	%end
</div>