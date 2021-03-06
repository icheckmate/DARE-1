<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en-US"> 
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> 
 
<title>DARE-Cactus</title> 
<link rel="stylesheet" href="${url('/newfiles/style000.css')}" type="text/css" media="screen" />
<link rel="stylesheet" type="text/css" media="all" href="${url('/newfiles/minimal_.css')}" />
 
<script type="text/javascript"> 
/* <![CDATA[ */
document.write('<style type="text/css">h1,h2,h3,h4,h5,#blurb,#site_name,#intro_blurb_title,#call_to_action,.light_gradient.dropcap1,.widgettitle,.dropcap2,.dark_gradient,th{text-indent:-9999px;}.noscript{display:none;}.bg_hover{background:none;}</style>');
/* ]]> */
</script> 

<meta name="disable_cufon" content="" />
<meta name="slider_speed" content="7000" />
<meta name="slider_disable" content="false" />
<meta name="slider_type" content="fading" />
 
<script type='text/javascript' SRC="${url('/newfiles/jquery00.js')}"></script>
<script type='text/javascript' SRC="${url('/newfiles/custom00.js')}"></script>
<script type='text/javascript' SRC="${url('/newfiles/cufon-yu.js')}"></script>
  
<!--[if IE 8]>
	<link rel="stylesheet" href="styles/_shared/ie8.css" type="text/css" media="screen" />
<![endif]--> 
 
<!--[if IE 7]>
	<link rel="stylesheet" href="styles/_shared/ie7.css" type="text/css" media="screen" />
<![endif]--> 

</head> 
 
<body > 
 
<div class="body_background"> 
	<div id="header"> 
		<div class="inner"> 
		
			<!-- logo -->
			<div id="logo"> 
				<a HREF="${url('/')}"><img SRC="${url('/newfiles/DARE0000.png')}" alt="" width="178" height="72" /></a>
			</div> 
			
			<!-- LOGIN -->
			<div id="social_header" style="top:121px;">
	% if c.userid=="false":
     <a href="${url('/users/login')}">Login</a><br/>
     <a href="${url('/users/register')}">Register</a>
	% else:
	<a href="${url('/users/logout')}">Logout</a><br/>
	%endif
			</div>		
			
			<!-- navigation -->
			<div id="main_navigation" class="jqueryslidemenu unitPng">
				<ul>
					  <li><a href="${url('/')}">HOME</a>
					  
					  </li>
                      <li><a href="${url('/cactus/about')}">ABOUT DARE-Cactus</a>
                         <ul>
            <li ><a title="Pipeline"  href="${url('/cactus/resources')}" >Resources</a></li>
            <li ><a title="Pipeline"  href="${url('/cactus/using_cactus')}" >Using Cactus</a></li>

                           </ul>
 
                      </li>


      <li><a href="${url('/cactus/contact')}">ACCOUNT</a>
         <ul>

            <li ><a title="Pipeline"  href="${url('/cactus/thorn_list')}" >Manage Thorn List</a></li>
            <li ><a title="Pipeline"  href="${url('/cactus/upload_thorn')}" >Upload Thorns</a></li>

        </ul>      
      </li>
% if c.userid!="false":      

%endif



      <li><a class="MenuBarItemSubmenu"> JOB SUBMISSION </a>
        <ul>

          <li ><a title="Pipeline"  href="${url('/cactus/cactus_form')}" >Cactus</a></li>

          <li><a href="${url('/cactus/job_table_view')}">Job Table View</a></li>
          
        </ul>
      </li>
      <li><a href="${url('/cactus/software')}">SOFTWARE</a></li>
      <li><a href="${url('/cactus/contact')}">CONTACT</a></li>

				</ul>
			</div> 
		</div><!-- inner --> 
	</div><!-- header --> 

	<div id="body_block" class="full_width fading framed minimal_soft_green"> 
	
			
		<div id="intro_blurb">
		<%  flash_message = h.flash.pop_message()  %>
   % if flash_message: 
     <div id="flash-message">${flash_message | h}</div>
   % endif

			<div class="inner">	
 			<!--	<a class="button_link alignright large_button" href=""><span>Learn More</span></a> -->	
 				${self.body()}

    </div><!-- inner --> 
		</div><!-- intro_blurb --> 
								
	</div><!-- body_block --> 
 
	<div id="footer"> 

	</div><!-- footer --> 
 
</div><!-- body_background --> 

</body> 
</html>
