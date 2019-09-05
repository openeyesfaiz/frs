<?php include 'inc/config.php'; ?>
<?php include 'inc/template_start.php'; ?>
<?php include 'inc/page_head.php'; ?>


<?php 
    $u_id = $_GET['id'] ;
    
    $config_params = parse_ini_file("config/config.ini");
    
    $conn = mysqli_connect($config_params['db_host'],$config_params['db_user'],$config_params['db_pwd'],$config_params['db_db']);
    
    if(! $conn){
        error_log('Could not connect: ' . mysqli_error());
        die('Could not connect: ' . mysqli_error());
    }else{
        error_log('Conn success');
    }
    
    $sql = 'SELECT * FROM enrolled_user WHERE frsid=' . $u_id . ';';
    $result = mysqli_query($conn, $sql);
    #error_log(gettype($result));

    if (mysqli_num_rows($result) == 1){
        while($row = mysqli_fetch_assoc($result)){
            $u_name = $row['name'];
            $u_image = $row['image'];
            $u_create_datetime = $row['create_datetime'];
        }
    }
?>
<?php 
    if(isset($_POST['del_hit_id'])){
        $post_del = $_POST['del_hit_id'];
        #error_log(is_numeric($post_del));
        if(is_numeric($post_del) == 1){
            $sql = 'DELETE FROM hit_image WHERE id=' . (int)$post_del . ';';
            if ($conn->query($sql) === TRUE){
                error_log("Record deleted successfully");
            }else{
                error_log("Error deleting record: " . $conn->error);
            }
        }
    }
?>

<div id="page-content">
    <div class="content-header">
        <ul class="nav-horizontal text-center">
        	<li>USER <?php echo $u_id ?></li>
        </ul>
	</div>
	
	<div class="row">
		<div class="col-lg-6">
			<div class="block">
                <div class="block-title">
                    <h2><i class="fa fa-pencil"></i> <strong>User</strong> Information</h2>
                </div>
                <form action="enrolled_home.php" method="post" class="form-horizontal form-bordered" onsubmit="frs_update(<?php echo $config_params['frs_host'] ?>,<?php echo $u_id ?>,<?php echo $u_name ?>);">
                    <div class="form-group">
                        <label class="col-md-3 control-label" for="user-id">UID</label>
                        <div class="col-md-9">
                        	<label id="user-id" name="user-id" class="form-control"><?php echo $u_id ?></label>
                        	<input type="hidden" id="user-id" name="user-id" class="form-control" value="<?php echo $u_id ?>">
                        </div>
					</div>
					
                    <div class="form-group">
                        <label class="col-md-3 control-label" for="user-name">NAME</label>
                        <div class="col-md-9">
                        	<input type="text" id="user-name" name="user-name" class="form-control" value="<?php echo $u_name ?>">
                        </div>
					</div>
					
                    <div class="form-group">
                        <label class="col-md-3 control-label" for="user-image">IMAGE</label>
                        <div class="col-md-9">
                        	<img src="data:image/gif;base64,<?php echo $u_image ?>"/>
                        </div>
					</div>
                    <div class="form-group form-actions">
                        <div class="col-md-9 col-md-offset-3">
                            <button type="submit" class="btn btn-sm btn-primary"><i class="fa fa-angle-right"></i> Modify</button>
                        </div>
                    </div>
				</form>
			</div>
		</div>
		
		<div class="col-lg-6">
			<div class="block">
                <div class="block-title">
                    <h2><i class="fa fa-pencil"></i> <strong>Hit</strong> Record</h2>
                </div>
                <?php 
                    $sql = 'SELECT * FROM hit_image WHERE enrolled_userid=' . $u_id . ' ORDER BY create_time desc;';
                    $get_hit = mysqli_query($conn, $sql);
                    #error_log(gettype($get_hit));
                ?>
                <table class="table table-bordered table-striped table-vcenter">
                    <tbody>
                    	<?php 
                        	if (mysqli_num_rows($get_hit) > 0){
                        	    while($row = mysqli_fetch_assoc($get_hit)){
                        	        $hit_id = $row['id'];
                        	        $hit_image = $row['image'];
                        	        $hit_score = $row['score'];
                        	        $hit_create_time = $row['create_time'];
                        	        $hit_uid = $row['enrolled_userid'];
                    	?>
                            <tr>
                                <td style="width: 20%;">
                                    <!--<a href="data:image/gif;base64,<?php echo $hit_image ?>" data-toggle="lightbox-image">
                                        <img src="data:image/gif;base64,<?php echo $hit_image ?>" alt="" class="img-responsive center-block" style="max-width: 110px;">
                                    </a>-->
                                    <img src="data:image/gif;base64,<?php echo $hit_image ?>" alt="" class="img-responsive center-block" style="max-width: 110px;">
                                </td>
                                <!--<td class="text-center">
                                    <label class="switch switch-primary">
                                        <input type="checkbox" checked><span></span>
                                    </label>
                                    Cover
                                </td>-->
                                <td>
                                	<label class="switch switch-primary">
                                		<p><?php echo $hit_create_time ?></p>
                                	</label>
                                </td>
                                <td class="text-center">
                                    <a href="#" onclick="del_record(<?php echo $u_id ;?>,<?php echo $hit_id ;?>)" class="btn btn-xs btn-danger"><i class="fa fa-trash-o"></i> Delete</a>
                                </td>
                            </tr>
                        <?php }} ?>
                    </tbody>
                </table>
			</div>
		</div>
		
	</div>
</div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="js/pages/enrolled_detail.js"></script>