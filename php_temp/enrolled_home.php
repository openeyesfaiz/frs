<?php include 'inc/config.php'; ?>
<?php include 'inc/template_start.php'; ?>
<?php include 'inc/page_head.php'; ?>

<?php
    $config_params = parse_ini_file("config/config.ini");
    
    $conn = mysqli_connect($config_params['db_host'],$config_params['db_user'],$config_params['db_pwd'],$config_params['db_db']);
    
    if(! $conn){
        error_log('Could not connect: ' . mysqli_error());
        die('Could not connect: ' . mysqli_error());
    }else{
        error_log('Conn success');
    }
?>
<?php 
    if(isset($_POST['user-name']) and isset( $_POST['user-id'])){
        $mod_user_name = $_POST['user-name'];
        $mod_user_id = $_POST['user-id'];
        if(is_null($mod_user_name) == FALSE){
            $sql = 'UPDATE enrolled_user SET name = "' . $mod_user_name . '" WHERE frsid = ' . $mod_user_id . ';';
            if ($conn->query($sql) === TRUE){
                error_log("Record updated successfully");
            }else{
                error_log("Error updating record: " . $conn->error);
            }
        }
    }
?>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="js/pages/enrolled_home.js"></script>
<?php 
    if(isset($_POST['del_u_id'])){
        $del_u_id = $_POST['del_u_id'];
        
        if(is_numeric($del_u_id) == 1){
            $sql = 'SELECT * FROM enrolled_user WHERE frsid=' . $del_u_id . ';';
            $result = mysqli_query($conn, $sql);
            if(mysqli_num_rows($result) == 1){
                while($row = mysqli_fetch_assoc($result)){
                    $search_ref_num = $row['ref_num'];
                    echo '<script>frs_u_delete("' . $config_params['frs_host'] . '","' . $row['ref_num'] . '","' . $del_u_id . '");</script>';
                }
            }
            
            $sql = 'DELETE FROM enrolled_user WHERE frsid=' . $del_u_id . ';';
            if ($conn->query($sql) === TRUE){
                error_log("User record deleted successfully");
            }else{
                error_log("Error deleting user record: " . $conn->error);
            }
        }
    }
?>

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
                			<p>DEL_U_ID is:<?php echo $del_u_id; ?></p>
                			<p>SEARCH REF NUM is <?php echo $search_ref_num ?></p>
                		</div>
                	</div>
                </div>
            </div>
		</div>
    </div>
    
    <div class="block full">
        <!-- All Orders Title -->
        <div class="block-title">
            <div class="block-options pull-right">
                <a href="javascript:void(0)" class="btn btn-alt btn-sm btn-default" data-toggle="tooltip" title="Settings"><i class="fa fa-cog"></i></a>
            </div>
            <h2><strong>All</strong> Enrolled Users</h2>
            <br/>
            <input class="form_action_button" type="button" value="Merge"/>
            <input class="form_action_button" type="button" value="Delete"/>
        </div>
        <!-- END All Title -->

        <!-- All Content -->
        <div>
        	Search View
        </div>
        <table id="enrolled_users" class="table table-bordered table-striped table-vcenter">
            <thead>
                <tr>
                	<th></th>
                    <th class="text-center" style="width: 100px;">ID</th>
                    <th class="visible-lg">Name</th>
                    <th class="text-center visible-lg">Image</th>
                    <th class="hidden-xs">Create Date</th>
                    <th class="text-right hidden-xs">Delete</th>
                    <!--<th>Status</th>
                    <th class="hidden-xs text-center">Submitted</th>
                    <th class="text-center">Action</th>-->
                </tr>
            </thead>
            <tbody>
            	<?php
                    $sql = 'SELECT * FROM enrolled_user;';
                    $result = mysqli_query($conn, $sql);
                    error_log(gettype($result));
            	?>
            	<?php if (mysqli_num_rows($result) > 0){
            	    while($row = mysqli_fetch_assoc($result)){
                ?>
    				<tr>
    					<td><input type="checkbox" id="c_<?php echo $row['frsid'] ?>"/></td>
    					<td onclick="window.location.href = 'enrolled_detail.php?id=<?php echo $row['frsid'] ?>'"><?php echo $row['frsid'] ?></td>
    					<td onclick="window.location.href = 'enrolled_detail.php?id=<?php echo $row['frsid'] ?>'"><?php echo $row['name'] ?></td>
    					<td onclick="window.location.href = 'enrolled_detail.php?id=<?php echo $row['frsid'] ?>'"><img src="data:image/gif;base64,<?php echo $row['image'] ?>"/></td>
    					<td><?php echo $row['create_datetime'] ?></td>
                        <td class="text-center">
                            <a href="#" onclick="del_u_record(<?php echo $row['frsid'] ?>)" class="btn btn-xs btn-danger"><i class="fa fa-trash-o"></i> Delete</a>
                        </td>
    				</tr>
    			<?php }} ?>
            </tbody>
        </table>
        <!-- END All Orders Content -->
    </div>
</div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="js/pages/enrolled_home.js"></script>

<link rel="stylesheet" type="text/css" href="css/pages/enrolled_home.css"/>