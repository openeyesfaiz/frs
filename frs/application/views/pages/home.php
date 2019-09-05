<?php 
    echo form_open('search/send', 'class="enroll_search_form"');
?>

<table class="search_form">
	<tr>
		<th>User ID</th>
		<td>
            <?php   
                $data = array(
                    'type'  =>  'number',
                    'name'  =>  'user_id',
                    'id'    =>  'search_id',
                    'class' =>  'search_id',
                    'label' =>  'User ID',
                    'min'   =>  '0',
                    'step'  =>  '1',
                );
                echo form_input($data);
            ?>
		</td>
	</tr>
	<tr>
		<th>Name</th>
		<td>
            <?php   
                $data = array(
                    'type'  =>  'text',
                    'name'  =>  'name',
                    'id'    =>  'search_name',
                    'class' =>  'search_name',
                    'label' =>  'Name',
                );
                echo form_input($data);
            ?>
		</td>
	</tr>
	<tr>
		<th>From Date</th>
		<td>
            <?php   
                $data = array(
                    'type'  =>  'date',
                    'name'  =>  'create_after',
                    'id'    =>  'search_create_after',
                    'class' =>  'search_create_after',
                    'label' =>  'Create After',
                );
                echo form_input($data);
            ?>
		</td>
	</tr>
	<tr>
		<th>To Date</th>
		<td>
            <?php   
                $data = array(
                    'type'  =>  'date',
                    'name'  =>  'create_before',
                    'id'    =>  'search_create_before',
                    'class' =>  'search_create_before',
                    'label' =>  'Create Before',
                );
                echo form_input($data);
            ?>
		</td>
	</tr>
</table>

<?php
    echo form_submit('searchsubmit', 'Search');
    echo form_close();
?>

<div id="result_field">
</div>