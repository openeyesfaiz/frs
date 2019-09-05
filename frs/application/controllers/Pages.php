<?php
class Pages extends CI_Controller{
    public function view($page = 'home'){
        
        if ( ! file_exists(APPPATH.'views/pages/'.$page.'.php'))
        {
            // Whoops, we don't have a page for that!
            show_404();
        }
        
        $data['title'] = ucfirst($page);
        
        $this->load->helper('url');
        $this->load->helper('form');

        $this->load->view('template/header', $data);
        $this->load->view('pages/'.$page, $data);
        $this->load->view('template/footer', $data);
    }
}
?>