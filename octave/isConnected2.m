%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%					   Two Mode Connection Check					   %
%						GOEKHAN POLAT (0830690)						   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% TODO: implement a function that determines whether a two-mode network is connected
% INPUT: adjacency matrix (mxn) of the two-mode network
% OUTPUT: Boolean 0 (false) or 1 (true)
function [is_connected] = isConnected2(network)
    is_connected = 1;

	% check zeros row
	for m=1:size(network)(1);
		line = 0;
		for n=1:1:size(network)(2);
			if network(m,n) == 1;
				line = 1;
			end;
		end;
				
		if line == 0;
		is_connected = 0;
		break;
		end;
	end;

	% check zeros column
	if(is_connected == 1)
		for m=1:size(network)(2);
			line = 0;
			for n=1:1:size(network)(1);
				if network(n,m) == 1;
					line = 1;
				end;
			end;
					
			if line == 0;
			is_connected = 0;
			break;
			end;
		end;
	end;
	
	% check connectivity
	set = [];	
	if(is_connected == 1)
		is_connected = 0;
		for i=1:1:size(network)(1);			
			for m=1:1:size(network)(1);
				for n=1:1:size(network)(2);
					if network(m,n) == 1;
						if size(set)(1) == 0;
						   set = [size(network)(1)+m,n];				   
						elseif intersect([size(network)(1)+m,n], set);
							tmp = [size(network)(1)+m,n];					
							set = union(set, tmp);
						end;
					end;
				end;
			end;
			if (size(set)(2) == size(network)(1)+size(network)(2))
			is_connected = 1;
			break;
			end;
		end;
	end;

end
