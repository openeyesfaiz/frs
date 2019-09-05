<?php include 'inc/config.php'; ?>
<?php include 'inc/template_start.php'; ?>
<?php include 'inc/page_head.php'; ?>

<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>

<!-- Page content -->
<div id="page-content">
    <!-- Dashboard Header -->
    <!-- For an image header add the class 'content-header-media' and an image as in the following example -->
    <div class="content-header">
        <div class="header-section">
            <div class="row">
                <div class="col-md-4 col-lg-6 hidden-xs hidden-sm">
                    <h1>Welcome <strong>Admin</strong><br><small>FRS</small></h1>
                </div>
                <div class="col-md-8 col-lg-6">
                	<div class="row text-center">
                		<div class="col-xs-4 col-sm-3">
                			<p>The camera IP is:<?php echo $camera_ip; ?></p>
                		</div>
                	</div>
                </div>
            </div>
		</div>
    </div>
    
    <div class="row">
        <div class="col-md-6">
            <!-- Camera View Widget -->
            <div class="widget">
				<div class="widget-extra themed-background-dark">
					<h3 class="widget-content-light">
						Camera View
					</h3>
				</div>
            </div>
			<div class="widget-extra-full">
				<div class="row text-center">
					<div class="col-xs-6 col-lg-3">
						<p>abcdef</p>
					</div>
				</div>
			</div>
		</div>
		<div class="col-md-6">
			<!-- Hit Record Widget -->
            <div class="widget">
				<div class="widget-extra themed-background-dark">
					<h3 class="widget-content-light">
						Hit Records
					</h3>
				</div>
            </div>
            <div class="widget-extra-full">
				<div class="row text-center">
					<div class="col-xs-6 col-lg-3">
						<p>fwerghrth</p>
					</div>
				</div>
            </div>
		</div>
    </div>
</div>

<script src="js/pages/frs_index.js"></script>