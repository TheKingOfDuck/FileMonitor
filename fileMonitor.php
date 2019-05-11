<?php
/*
-------------------------------------------------
   File Name：     fileMonitor
   Description :
   Author :       CoolCat
   date：          2019/1/3
-------------------------------------------------
   Change Activity:
                   2019/1/3:
-------------------------------------------------
*/
class FileMonitor
{
	private $dir;
	private $i=0;
	private $files = [];
	private $filesize = [];
	public function __construct($argv)
	{
		$this->dir = $this->getparam($argv);
		$this->getfiles($this->dir);
		print "[+] total:".count($this->files[$this->i])."\n\r";
		$this->i++;
		while(true)
		{
			$this->getfiles($this->dir);
			if(isset($this->files[$this->i-1]) && ((count($this->files[$this->i])>count($this->files[$this->i-1]))))
			{
				print "[+] total:".count($this->files[$this->i])."\n\r";
				print "[*] addfile: ".implode('|',array_diff($this->files[$this->i],$this->files[$this->i-1]))."\n\r";
			}
			if(isset($this->files[$this->i-1]) && ((count($this->files[$this->i])<count($this->files[$this->i-1]))))
			{
				print "[+] total:".count($this->files[$this->i])."\n\r";
				print "[*] deletefile: ".implode('|',array_diff($this->files[$this->i-1],$this->files[$this->i]))."\n\r";
			}
			if(isset($this->filesize[$this->i-1]))
			{
				array_map(function($v,$val,$key){
					if($v != $val)
					{
						print "[*] updatefile:{$key}\n\r";
					}
				},$this->filesize[$this->i-1],$this->filesize[$this->i],array_keys($this->filesize[$this->i]));
			}
			$this->i++;
			if($this->i>=30)
			{
				$this->files = [];
				$this->filesize = [];
				$this->i = 0;
			}
		}
	}

	private function getparam($argv)
	{
		foreach($argv as $key=>$val)
		{
			if($val == "--dir")
			{
				return is_dir($argv[$key+1])?$argv[$key+1]:exit("[-] directory does not exist!");
			}
		}
	}

	private function getfiles($dir)
	{
		if(is_dir($dir))
		{
			$d = scandir($dir);
			foreach($d as $v)
			{
				if($v != '.' && $v != '..')
				{
					if(is_dir("{$dir}/{$v}"))
					{
						$this->getfiles("{$dir}/{$v}");	
					}
					else
					{
						$this->files[$this->i][] = "{$dir}/{$v}";
						$this->filesize[$this->i]["{$dir}/{$v}"] = filesize("{$dir}/{$v}");
					}
				}
			}
		}
		else
		{
			$this->files[$this->i][] = $dir;
			$this->filesize[$this->i][$dir] = filesize($dir);
		}
	}
}
print " 
    _____________
   < FileMonitor >
    -------------
      /\_)o<
     |       | 
     | O . O |
      \_____/
    By CoolCat
";
new FileMonitor($argv);
?>