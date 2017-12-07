clear variables
%% Set paths
template_directory = '<?=$template_directory;?>';
working_directory='<?=$working_directory;?>';

%% Make a list of all c3d files in the working directory
all_files = dir(fullfile(working_directory, '*.mat'));

file_list=[];
file_count=0;
for i=1:length(all_files)
       [~, name, extension]=fileparts(all_files(i).name);
       if ~strcmp(all_files(i).name, 'Static 1.mat') %we ignore the file static.c3d
           file_count = file_count + 1;
           file_list{file_count} = [all_files(i).name];
       end
end

if isempty(file_list)
    warning('No dynamic files could be found. Check that the correct folder was selected and that both .1.c3d and .c3d file are available.')
end

%% Find the static file
static_count=0;
dynamic_count=0;

for i=1:length(file_list)
    if strcmpi(file_list{i}(1), 'S')
        static_count=static_count+1;
        static_list{static_count}=file_list{i};
    else
        dynamic_count=dynamic_count+1;
        dynamic_list{dynamic_count}=file_list{i};
    end
end

%% Check that required files are present
if dynamic_count == 0
    error('No dynamic trials found.')
end

%% load fle
dynamic_file = file_list{1};
file_full = load(strcat(working_directory,dynamic_file));

%% read from the file
captureFq = file_full.Dynamic_1.FrameRate;

%% save to xml
docNode = com.mathworks.xml.XMLUtils.createDocument('metrics');
docRootNode = docNode.getDocumentElement;
thisElement = docNode.createElement('capture_frequency'); 
thisElement.appendChild(docNode.createTextNode(num2str(captureFq)));
docRootNode.appendChild(thisElement);

xmlFileName = 'output.xml';
xmlwrite(xmlFileName,docNode);
%type(xmlFileName);