%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%					   One Mode Connection Check					   %
%						GOEKHAN POLAT (0830690)						   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% TODO: implement a function that determines whether a one-mode network is connected
% INPUT: adjacency matrix (nxn) of the one-mode network
% OUTPUT: Boolean 0 (false) or 1 (true)
function [is_connected] = isConnected1(network)
    is_connected = 0;
    is_symmetric = 1;

    % check symmetry    
    for m=1:1:size(network)(1);
		if network(m,m) != 0;
			is_symmetric = 0;
			break;
		end;    
		for n=1:1:size(network)(2);
		    if m != n;
				if network(m,n) != network(n,m);
					is_symmetric = 0;
					break;
				end;
			end;
		end;
	end;

    % check connectiveness  
    if is_symmetric;  
		set = [];    
		for m=1:1:size(network)(1);
			for n=1:1:size(network)(2);
				if network(m,n) == 1;
					if size(set)(1) == 0;
					   set = [m,n];
					elseif intersect([m,n], set);
						tmp = [m,n];
						set = union(set, tmp);									
					end;
				end;
			end;
			
			if size(set)(2) == size(network)(1);
				is_connected = 1;
				break;				
			end;
		end;
	end;

end;
