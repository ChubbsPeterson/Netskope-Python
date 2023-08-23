from endpoints.endpoint_steering import Steering
from endpoints.endpoint_ubadatasvc import UbaDataSvc
from endpoints.endpoint_atp import ATP
from endpoints.endpoint_drm import DRM
from endpoints.endpoint_incidents import Incidents
from endpoints.endpoint_profiles import Profiles
from endpoints.endpoint_nsiq import Nsiq
from endpoints.endpoint_scim import Scim
from endpoints.endpoint_platform import Platform
from endpoints.endpoint_policy import Policy
from endpoints.endpoint_infrastructure import Infrastructure
from endpoints.endpoint_events import Events
from endpoints.endpoint_services import Services

TENANT = 'tenant_name'
BASE_URL = f"https://{TENANT}.goskope.com/api/v2" 
AUTH_TOKEN = "api_token"

# Initialize individual endpoints
steering_client = Steering(base_url=BASE_URL, auth_token=AUTH_TOKEN)
ubadatasvc_client = UbaDataSvc(base_url=BASE_URL, auth_token=AUTH_TOKEN)
atp_client = ATP(base_url=BASE_URL, auth_token=AUTH_TOKEN)
drm_client = DRM(base_url=BASE_URL, auth_token=AUTH_TOKEN, instance="test")
incidents_client = Incidents(base_url=BASE_URL, auth_token=AUTH_TOKEN)
profiles_client = Profiles(base_url=BASE_URL, auth_token=AUTH_TOKEN)
nsiq_client = Nsiq(base_url=BASE_URL, auth_token=AUTH_TOKEN)
scim_client = Scim(base_url=BASE_URL, auth_token=AUTH_TOKEN)
platform_client = Platform(base_url=BASE_URL, auth_token=AUTH_TOKEN)
policy_client = Policy(base_url=BASE_URL, auth_token=AUTH_TOKEN)
infrastructure_client = Infrastructure(base_url=BASE_URL, auth_token=AUTH_TOKEN)
events_client = Events(base_url=BASE_URL, auth_token=AUTH_TOKEN)
services_client = Services(base_url=BASE_URL, auth_token=AUTH_TOKEN)

def to_epoch_time(time_str=None, subtract=None):
    """
    Convert provided time or 'now' to Epoch time.

    Args:
    - time_str (str): Time string in the format "MM-DD-YY HH:mm" or 'now'. If None, defaults to 'now'.
    - subtract (dict): Dictionary specifying the time delta to subtract. E.g. {'hours': 2, 'minutes': 30}

    Returns:
    - int: Epoch time
    """
    # If no time string is provided or it's 'now', use the current time
    if not time_str or time_str == 'now':
        dt = datetime.datetime.now()
    else:
        dt = datetime.datetime.strptime(time_str, "%m-%d-%y %H:%M")

    # Subtract timedelta if provided
    if subtract:
        delta = datetime.timedelta(**subtract)
        dt -= delta

    # Return as epoch time
    return int(dt.timestamp())

"""
Steering Client Endpoint Testing
"""
#steering_client.get_gre_pops(display_output=True) # Get all GRE POPs
#steering_client.get_gre_pop(id, display_output=True) # Get a specific GRE POP by ID, ex. 0X00D3
#steering_client.get_gre_tunnels(display_output=True) # Get GRE tunnels list
#steering_client.create_gre_tunnel(data, display_output=True) # Create GRE tunnel <---payload---> {"site":"string","srcipidentity":"string","pops":["string"],"vendor":"string","template":"string","sourcetype":"string","notes":"string","enable":true,"options":{"xff":{"enable":false,"iplist":["string"]}}}
#steering_client.get_gre_tunnel(id, display_output=True) # Get GRE tunnel
#steering_client.update_gre_tunnel(id, data, display_output=True) # Update GRE tunnel <---payload ---> { "status": 200, "result": "string", "data": [ { "id": 1, "site": "string", "vendor": "string", "template": "string", "sourcetype": "string", "notes": "string", "srcipidentity": "string", "pops": [ { "name": "string", "gateway": "string", "probeip": "string", "primary": true, "usertrafficStatus": "string", "usertrafficLast": "string", "keepaliveStatus": "string", "keepaliveLast": "string", "throughput": "string" } ], "enabled": true, "options": { "xff": { "enabled": false, "iplist": [ "string" ] } }, "version": 2 } ] }
#steering_client.delete_gre_tunnel(id, display_output=True) # Delete GRE tunnel
#steering_client.get_ipsec_pops(display_output=True) # Get IPSec points of presence(POPs) list
#steering_client.get_ipsec_pop(id, display_output=True) # Get IPSec points of presence(POPs) list
#steering_client.get_ipsec_tunnels(display_output=True) # Get IPSec tunnels
#steering_client.create_ipsec_tunnel(data, display_output=True) # Create IPSec tunnel
#steering_client.get_ipsec_tunnel(id, display_output=True) # Get specific IPSec tunnel
#steering_client.update_ipsec_tunnel(id, data, display_output=True) # Update IPSec tunnel
#steering_client.delete_ipsec_tunnel(id, display_output=True) # Delete IPSec tunnel
#steering_client.get_private_apps(display_output=True) # Get list of private applications
#steering_client.create_private_app(data, display_output=True) # Create a private application
#steering_client.delete_private_app(private_app_id, display_output=True)  # Delete a private application
#steering_client.update_private_app(private_app_id, data, display_output=True) # Update a private application
#steering_client.patch_private_app(private_app_id, data, display_output=True) # Patch a private application
#steering_client.get_private_app(private_app_id, display_output=True) # Get a private application
#steering_client.retrieve_policy_in_use_for_private_apps(data, display_output=True)  # Retrieve number of policy in use for specified private apps <---payload---> { "ids": [ "string" ] }  !!!! (actually int)
#steering_client.create_tags_for_private_apps(data, display_output=True) # Bulk create tags to associate with specified private apps
#steering_client.bulk_update_tags_for_private_apps(data, display_output=True) # Bulk update tags to associate with specified private apps
#steering_client.bulk_delete_tags_for_private_apps(data, display_output=True) # Bulk delete tags for specified private apps
#steering_client.get_list_of_private_app_tags(display_output=True) # Get list of private app tags
#steering_client.get_private_app_tag(tag_id, display_output=True) # Get a private app tag based on tag id
#steering_client.update_private_app_tag_based_on_id(tag_id, data, display_output=True) # Update a private app tag based on tag id
#steering_client.delete_private_app_tag_based_on_id(tag_id, display_output=True) # Delete a private app tag based on tag id
#steering_client.retrieve_policy_in_use_for_tags(data, display_output=True) # Retrieve number of policy in use for specified tags

"""
ATP Endpoint Testing
"""
#file_path = "path_to_your/NTRadPing.exe"  # Replace with the path to your file
#file_type = "application/x-msdownload"  # MIME type of the file
#response = atp_client.file_scan(file_path, file_type, display_output=True) # API to submit a file for scan by Netskope sandbox(supported file types: .exe, file size: up to 16MB, up to 1000 files per day).
#jobid = response.get('jobid') # Extract jobid from the response
#atp_client.get_scan_report(jobid, display_output=True) # Get analysis report of a file submitted for scan by sandbox, Using jobid returned in filescan request (Up to 10,000 requests per day).

"""
DRM Endpoint Testing
"""
#drm_client.list_labels(display_output=True) #Fetches and returns the list of labels from the DRM SaaS vendor.
#drm_client.list_labels(vendor="other_vendor_name", display_output=True) # Optionally, you can specify another vendor

"""
Incidents Endpoint Testing
"""
#incidents_client.get_anomaly(anomalyId, display_output=True) # Get the anomaly by anomalyId.
#incidents_client.allow_anomaly(anomalyId, display_output=True) # It is a generic API to mark anomaly as allowed. For UCI Impact, it will revert the impact ingestion.
#incidents_client.get_anomalies(data, display_output=True) # Get a list of anomalies. It will return anomalies within 90 days. <---payload---> { "filters": { "user": { "equals": [ "string" ] }, "source": { "equals": [ "string" ] }, "startTime": { "equals": 0 }, "endTime": { "equals": 0 }, "anomalyId": { "equals": [ "string" ] } } }
#incidents_client.get_uci(display_output=True) # Get a list of users confidence index.
#incidents_client.user_uci_impact(data_payload, display_output=True) # Trigger the uci compute process after receiving uci impact request. <---payload---> { "user": "string", "score": 0, "timestamp": 0, "source": "string", "reason": "string" }

"""
Profiles Endpoint Testing
"""
#profiles_client.get_profile(profile_id, display_output=True) # Get single list resource by ID.
#profiles_client.update_profile(profile_id, data_payload, display_output=True) # Partial update on fields, given action will replace to values field.
#profiles_client.delete_profile(profile_id, display_output=True) # Delete single list by ID
#profiles_client.get_all_profiles(display_output=True) # Return all list objects, recommended to restrict the fields returned with &fields=id,name,description.
#profiles_client.create_profile(data_payload, display_output=True) # Create single list resource. Required attributes: Name, Type, and Values. Current list types supported: Domains - List objects which include only domain values and optional comment. <---payload---> { "name": "search engines domains", "description": "all of search engines websites", "type": "domain", "values": [ { "value": "*.google.com", "comment": "search engine" }, { "value": "www.yahoo.com" }, { "value": "www.facebook.com", "comment": "social media" } ] }

"""
NSIQ Endpoint Testing
"""
#nsiq_client.ioc_info(hash_value, display_output=True) # Get single sample information.
#nsiq_client.batch_ioc_info(hash_list, display_output=True) # Get sample information in batch. <---payload---> { "hash": [ "ba5aa2352bf1132e0fd3e58680eafa8e912b0c56b9919b211fd84878e615798e", "4aacabe02537f435d83be4d180751234" ] }
#nsiq_client.ioc_report(hash_value, display_output=True) # Get sample report.
#nsiq_client.get_recategorizations(display_output=True) # List the re-categorization requests.
# nsiq_client.post_recategorizations(data, display_output=True) # Submit url re-categorization requests. <---payload---> { "justification": "test", "email": "user@netskope.com", "recat_requests": [ { "url": "netskope.com", "suggested_categories": [ "Technology", "Security" ] }, { "url": "example.com", "suggested_categories": [ "Technology", "Business" ] }, { "url": "example.net", "suggested_categories": [ "Business" ] } ] }
#nsiq_client.get_recategorization(id_value, display_output=True) # Get the re-categorization request details by id.
#nsiq_client.get_recategorization_url(id_value, url_id, display_output=True) # Get the status of the url under a re-categorization request by id.

""" 
SCIM Endpoint Testing
"""
#scim_client.create_user(data, display_output=True) # Creation of a SCIM User. <---payload---> { "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:User" ], "userName": "upn1", "name": { "familyName": "last_name", "givenName": "first_name" }, "active": true, "emails": [ { "value": "email1@netskope.local", "primary": true } ], "externalId": "User-Ext_id", "meta": { "resourceType": "User" } }
#scim_client.get_users(display_output=True) # Get Scim Users.
#scim_client.replace_user(id_value, data, display_output=True) # Replace existing SCIM record for {id}. <---payload---> { "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:User" ], "userName": "upn1", "name": { "familyName": "last_name", "givenName": "first_name" }, "active": true, "emails": [ { "value": "email1@netskope.local", "primary": true } ], "externalId": "User-Ext_id", "meta": { "resourceType": "User" } }
#scim_client.get_user(id_value, display_output=True) # Get the Scim User.
#scim_client.update_user(id_value, data, display_output=True) # Update existing SCIM User record by {id}. <---payload---> { "schemas": [ "urn:ietf:params:scim:api:messages:2.0:PatchOp" ], "Operations": [ { "path": "userName", "op": "add", "value": { "value": "new_upn" } } ] }
#scim_client.delete_user(id_value, display_output=True) # Delete SCIM User record by {id}.
#scim_client.create_group(data, display_output=True) # Create new SCIM Group. <---payload---> { "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:Group" ], "displayName": "sample_group1", "members": [ { "value": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" } ], "externalId": "Group-Ext_id", "meta": { "resourceType": "Group" } }
#scim_client.get_groups(display_output=True) # Get SCIM Groups.
#scim_client.replace_group(id_value, data, display_output=True) # Replace existing SCIM Group for {id}. <---payload---> { "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:Group" ], "displayName": "sample_group1", "members": [ { "value": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" } ], "externalId": "Group-Ext_id", "meta": { "resourceType": "Group" } }
#scim_client.get_group(id_value, display_output=True) # Get SCIM Group by {id}.
#scim_client.update_group(id_value, data, display_output=True) #  <---payload---> { "schemas": [ "urn:ietf:params:scim:api:messages:2.0:PatchOp" ], "Operations": [ { "path": "members", "op": "add", "value": { "value": { "value": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" } } } ] }
#scim_client.delete_group(id_value, display_output=True) # Delete SCIM Group record by {id}.

"""
Platform Endpoint Testing
"""
#platform_client.get_all_roles(display_output=True) # Find all predefined roles.
#platform_client.get_role_by_id(role_id, display_output=True) # Predefined role by id.
#platform_client.get_all_v2_roles(display_output=True) # All predefined v2 roles.
#platform_client.get_v2_role_by_id(role_id, display_output=True) # Get predefined v2 roles by id.
#platform_client.get_all_custom_roles(display_output=True) # Get all custom roles.
#platform_client.create_custom_role(data, display_output=True) # Create custom role. <---payload---> { "role_id": 0, "role_type": "string", "role_name": "string", "role_description": "string", "last_edited": "Unknown Type: Date", "obfuscation_type": "string", "permissions": [ { "id": 0, "role_id": 0, "role_function_sub_function_assoc_page_assoc_id": 0, "permission": "string" } ] }
#platform_client.update_custom_role(data, display_output=True) # Update custom role. <---payload---> { "role_id": 0, "role_type": "string", "role_name": "string", "role_description": "string", "last_edited": "Unknown Type: Date", "obfuscation_type": "string", "permissions": [ { "id": 0, "role_id": 0, "role_function_sub_function_assoc_page_assoc_id": 0, "permission": "string" } ] }
#platform_client.get_custom_role_by_id(role_id, display_output=True) # Get custom role by id.
#platform_client.delete_custom_role_by_id(role_id, display_output=True) # Delete custom role by id.
#platform_client.get_admin_domains(display_output=True) # Get a list of admin domains.
#platform_client.get_all_idp_accounts(display_output=True) # Get a list of all IDP accounts configured for SSO.
#platform_client.create_idp_account(data, display_output=True) # Create a new IDP account for SSO. <---payload---> { "name": "string", "isEnabled": true, "idpUrl": "string", "idpEntityId": "string", "idpCertificate": "string", "alternativeUserEmailAttribute": "string", "isSsoSigned": true, "shouldForceAuthn": true, "isStrictSso": true, "isSloEnabled": true, "isSloSigned": true, "idpSloUrl": "string", "isAdfsSlo": true, "allowedRoles": [ 0 ], "domainMapping": [ 0 ], "status": "draft" }
#platform_client.update_idp_account(id_value, data, display_output=True) # Partial update an existing IDP account for SSO. <---payload---> { "name": "string", "isEnabled": true, "idpUrl": "string", "idpEntityId": "string", "idpCertificate": "string", "alternativeUserEmailAttribute": "string", "isSsoSigned": true, "shouldForceAuthn": true, "isStrictSso": true, "isSloEnabled": true, "isSloSigned": true, "idpSloUrl": "string", "isAdfsSlo": true, "allowedRoles": [ 0 ], "domainMapping": [ 0 ], "status": "draft", "id": "string" }
#platform_client.delete_idp_account(id_value, display_output=True) # Delete an existing IDP account for SSO.

"""
Policy Endpoint Testing
"""
#policy_client.get_domain_fronting_exception_by_id(id, display_output=True) # Get Domain Fronting exceptions by ID.
#policy_client.update_domain_fronting_exception(id, data, display_output=True) # Update Domain Fronting exceptions. <---payload---> { "name": "my-exception", "description": "my domain fronting description", "lists": [ "199", "1978" ] }
#policy_client.delete_domain_fronting_exception_by_id(id, display_output=True) # delete_domain_fronting_exception_by_id
#policy_client.get_domain_fronting_exceptions(display_output=True) # Get Domain Fronting exceptions.
#policy_client.create_domain_fronting_exception(data, display_output=True) # Create Domain Fronting Exception. <---payload---> { "name": "my-exception", "description": "my domain fronting description", "lists": [ "199", "1978" ] }
#policy_client.get_npa_policies(display_output=True) # Get list of npa policies.
#policy_client.create_npa_policy(data, display_output=True) # Create a npa policy. <---payload---> { "name": "my-exception", "description": "my domain fronting description", "lists": [ "199", "1978" ] }
#policy_client.delete_npa_policy(id, display_output=True) # Delete a npa policy.
#policy_client.patch_npa_policy(id, data, display_output=True) # Patch a npa policy. <---payload---> { "rule_name": "vantest", "description": "any", "rule_data": { "users": [ "vphan@netskope.com" ], "excludedUsers": [ "someone@netskope.com" ], "userType": "user", "access_method": "Client", "policy_type": "private-app", "privateApps": [ "app1", "app2" ], "privateAppIds": [ "100", "201" ], "privateAppTags": [ "tag1", "tag2" ], "privateAppTagIds": [ "1", "2" ], "privateAppsWithActivities": [ { "appName": "[172.31.12.135]", "activities": [ { "activity": "any", "list_of_constraints": [] } ] } ], "match_criteria_action": { "action_name": "allow" }, "classification": "string", "show_dlp_profile_action_table": true, "external_dlp": true, "net_location_obj": [ "190.123.150.10", "190.218.0.0/16" ], "b_negateNetLocation": true, "srcCountries": [ "US", "AF", "CN" ], "b_negateSrcCountries": true, "json_version": 3, "version": 1 }, "rule_order": 1, "group_id": "1" }
#policy_client.get_npa_policy(id, display_output=True) # Get a npa policy.
#policy_client.get_all_url_lists(display_output=True) # Get all applied and pending URL lists.
#policy_client.create_url_list(data, display_output=True) # Create a new URL list. <---payload---> { "name": "string", "data": { "urls": [ "www.test.com" ], "type": "exact" } }
#policy_client.upload_url_list_config(file_path, display_output=True) # Upload multiple configurations via a JSON file.
#policy_client.get_url_list_by_id(id, display_output=True) # Get URL list by ID.
#policy_client.replace_url_list(id, data, display_output=True) # Replace a URL list configuration. <---payload---> { "name": "string", "data": { "urls": [ "www.test.com" ], "type": "exact" } }
#policy_client.delete_url_list(id, display_output=True) # Delete a URL list.
#policy_client.patch_url_list(id, action, data=None, display_output=True) # Patch URL list.
#policy_client.apply_pending_url_changes(display_output=True) # Apply pending URL list changes.

"""
Infrastructure Endpoint Testing
"""
#infrastructure_client.get_publishers(display_output=True) # Get list of publisher objects.
#infrastructure_client.create_publisher(data, display_output=True) # Create a publisher. <---payload---> { "name": "string", "lbrokerconnect": false, "tags": [ { "tag_name": "string" } ] }
#infrastructure_client.delete_publisher(publisher_id, display_output=True) # Delete a publisher.
#infrastructure_client.update_publisher(publisher_id, data, display_output=True) # Update a publisher. <---payload---> { "name": "string", "id": 0, "lbrokerconnect": true, "tags": [ { "tag_id": 0, "tag_name": "string" } ] }
#infrastructure_client.patch_publisher(publisher_id, data, display_output=True) # Patch a publisher. <---payload---> { "name": "string", "id": 0, "lbrokerconnect": true, "tags": [ { "tag_id": 0, "tag_name": "string" } ] }
#infrastructure_client.get_publisher(publisher_id, display_output=True) # Get a publisher.
#infrastructure_client.generate_publisher_registration_token(publisher_id, display_output=True) # Generate and retrieve a token for publisher registration.
#infrastructure_client.get_publisher_upgrade_profiles(display_output=True) # Get list of publisher upgrade profile objects.
#infrastructure_client.create_publisher_upgrade_profile(data, display_output=True) # Create a publisher upgrade profile. <---payload---> { "name": "string", "frequency": "string", "timezone": "string", "docker_tag": "string", "release_type": "string", "enabled": 0 }
#infrastructure_client.delete_publisher_upgrade_profile(upgrade_profile_id, display_output=True) # Delete a publisher.
#infrastructure_client.update_publisher_upgrade_profile(upgrade_profile_id, data, display_output=True) # Update a publisher upgrade profile. <---payload---> { "name": "string", "id": 0, "frequency": "string", "timezone": "string", "docker_tag": "string", "release_type": "string", "enabled": 0 }
#infrastructure_client.get_publisher_upgrade_profile(upgrade_profile_id, display_output=True) # Get a publisher upgrade profile.

"""
Events Endpoint Testing
"""
#end_time = to_epoch_time() # Epoch timestamp for now
#start_time = to_epoch_time('now', subtract={'days': 30}) # # Epoch timestamp for 30 days ago

#events_client.get_alerts(type_="DLP", acked="false", limit=10, offset=15, insertionstarttime=start_time, insertionendtime=end_time, display_output=True)#events_client.get_application_events(display_output=True) # Get application events generated by Netskope
#events_client.get_audit_events(display_output=True) # Get audit events generated by Netskope
#events_client.get_exported_alert_events(display_output=True) # Export alerts generated by Netskope
#events_client.get_exported_application_events(display_output=True) # Export application events generated by Netskope
#events_client.get_exported_audit_events(display_output=True) # Export audit events generated by Netskope
#events_client.get_exported_connection_events(display_output=True) # Export connection events generated by Netskope
#events_client.get_exported_incident_events(display_output=True) # Export DLP incidents generated by Netskope
#events_client.get_exported_infrastructure_events(display_output=True) # Export infrastructure events generated by Netskope
#events_client.get_exported_network_events(display_output=True) # Export network events generated by Netskope
#events_client.get_exported_page_events(display_output=True) # Export page events generated by Netskope
#events_client.export_alerts_uba(display_output=True) # Export alerts generated by Netskope of type UBA
#events_client.export_alerts_security_assessment(display_output=True) # Export alerts generated by Netskope of type Security Assessment
#events_client.export_alerts_quarantine(display_output=True) # Export alerts generated by Netskope of type quarantine
#events_client.export_alerts_remediation(display_output=True) # Export alerts generated by Netskope of type remediation
#events_client.export_alerts_policy(display_output=True) # Export alerts generated by Netskope of type policy
#events_client.export_alerts_malware(display_output=True) # Export alerts generated by Netskope of type malware
#events_client.export_alerts_malsite(display_output=True) # Export alerts generated by Netskope of type malsite
#events_client.export_alerts_compromised_credential(display_output=True) # Export alerts generated by Netskope of type Compromised Credential
#events_client.export_alerts_ctep(display_output=True) # Export alerts generated by Netskope of type ctep/ips/c2
#events_client.export_alerts_dlp(display_output=True) # Export alerts generated by Netskope of type DLP
#events_client.export_alerts_watchlist(display_output=True) # Export alerts generated by Netskope of type watchlist
#events_client.get_infrastructure_events(display_output=True) # Get infrastructure events generated by Netskope
#events_client.get_network_events(display_output=True) # Get network events generated by Netskope
#events_client.get_page_events(display_output=True) # Get page events generated by Netskope
#events_client.retrieve_transaction_events_token(display_output=True) # Retrieve subscription key and path for Netskope transaction events

"""
Services Endpoint Testing
"""
#services_client.get_cci_app_info(display_output=True) # Get CCI related application information based on the apps/category/ccl/connector/discovered/domain/ids/tag.
#services_client.get_cci_domain(display_output=True) # Get the steering & discovery domains for the application/id.
#services_client.get_cci_tags(display_output=True) # Get tags for the list of applications/ids.
#services_client.create_cci_tags(data, display_output=True) # Creates new tag and associate the same to the list of applications/ids. <---payload---> { "tag": "ccl_high", "apps": [ "Box", "Amazon Database" ], "ids": [ 1, 2 ] }
#services_client.add_cci_tags(tag, data, display_output=True) # Add existing tag to the list of applications/ids. <---payload---> { "apps": [ "Box", "Amazon Database" ], "ids": [ 1, 2 ], "action": "append" }
#services_client.get_pending_bandwidth_changes(display_output=True) # Get bandwidth control pending changes.
#services_client.apply_bandwidth_changes(data, display_output=True) # Apply bandwidth control pending changes. <---payload---> { "links": [ 1 ], "traffic_classes": [ 1 ], "policies": [ 1 ], "traffic_class_rules": [ 1 ] }
#services_client.create_bandwidth_links(data, display_output=True) # Create bandwidth control links. <---payload---> [ { "name": "link1", "definition": { "ipsec_sites": [ "ipsec_site1" ] }, "size": "100 mbps" } ]
#services_client.update_bandwidth_links(data, display_output=True) # Update bandwidth control links. <---payload---> [ { "id": 1, "name": "link1", "definition": { "ipsec_sites": [ "ipsec_site1" ] }, "size": "100 mbps" } ]
#services_client.delete_bandwidth_control_link(data, display_output=True) # Delete a bandwidth control link.  <---payload---> [ 1 ]
#services_client.get_bandwidth_control_link(data, display_output=True) # Get bandwidth control link.  <---payload---> { "filters": { "name": { "value": "Link_name", "operator": "like" }, "ipsec_site": { "value": [ "Site1" ] }, "last_edit": { "value": { "starttime": "2023-01-30 06:01:01", "endtime": "2023-01-30 07:01:01" } } } }
#services_client.get_bandwidth_control_link(link_id, display_output=True) # Get bandwidth control link.
#services_client.update_bandwidth_control_link(link_id, data, display_output=True) # Update a bandwidth control link. <---payload---> [ { "name": "link1", "definition": { "ipsec_sites": [ "ipsec_site1" ] }, "size": "100 mbps" } ]
#services_client.delete_bandwidth_control_link(link_id, display_output=True) # Delete a bandwidth control link.
#services_client.create_bandwidth_control_policies(data, display_output=True) # Create bandwidth control policies. <---payload---> [ { "name": "policy1", "links": [ "link1" ], "all_links": false, "bandwidth_limits": [ { "traffic_class": "traffic_class1", "max_bandwidth": "100 mbps", "type": "exact" } ], "enabled": true, "order": 1 } ]
#services_client.update_bandwidth_control_policies(data, display_output=True) # Update bandwidth control policies. <---payload---> [ { "id": 1, "name": "policy1", "links": [ "link1" ], "all_links": false, "bandwidth_limits": [ { "traffic_class": "traffic_class1", "max_bandwidth": "100 mbps", "type": "exact" } ], "enabled": true } ]
#services_client.delete_bandwidth_control_policies(data, display_output=True) # Delete bandwidth control policies. <---payload---> [ 1 ]
#services_client.list_bandwidth_control_policies(data, display_output=True) # Get bandwidth control policies list. <---payload---> { "filters": { "name": { "value": "policy_name", "operator": "like" }, "link": { "value": [ "Link1" ] }, "traffic_class": { "value": [ "Class1" ] }, "last_edit": { "value": { "starttime": "2023-01-30 06:01:01", "endtime": "2023-01-30 07:01:01" } } } }
#services_client.get_bandwidth_control_policy(policy_id, display_output=True) # Get bandwidth control policy.
#services_client.update_bandwidth_control_policy(policy_id, data, display_output=True) # Update a bandwidth control policy. <---payload---> { "name": "policy1", "links": [ "link1" ], "all_links": false, "bandwidth_limits": [ { "traffic_class": "traffic_class1", "max_bandwidth": "100 mbps", "type": "exact" } ], "enabled": true, "order": 1 }
#services_client.delete_specific_bandwidth_control_policy(policy_id, display_output=True) # Delete bandwidth control policies.
#services_client.create_bandwidth_control_trafficclasses(data, display_output=True) # Create bandwidth control trafficclasses. <---payload---> [ { "name": "traffic_class1", "description": "description" } ]
#services_client.update_bandwidth_control_trafficclasses(data, display_output=True) # Update bandwidth control trafficclasses. <---payload---> [ { "id": 1, "name": "traffic_class1", "description": "description" } ]
#services_client.list_bandwidth_control_trafficclasses(display_output=True) # Get bandwidth control trafficclasses list.
#services_client.delete_bandwidth_control_trafficclasses(data, display_output=True) # Delete bandwidth control trafficclasses. <---payload---> [ 1 ]
#services_client.get_bandwidth_control_traffic_class(class_id, display_output=True) # Get bandwidth control traffic class rule.
#services_client.update_bandwidth_control_trafficclass(class_id, data, display_output=True)
#services_client.delete_bandwidth_control_trafficclass(class_id, display_output=True)
#services_client.create_bandwidth_control_traffic_class_rules(data, display_output=True) # Create bandwidth control traffic class rules. <---payload---> [ { "source": { "user": [ "user1" ], "user_group": [ "user_group1" ], "organization_unit": [ "organization_unit1" ], "exclude_user": [ "user1" ], "exclude_user_group": [ "user_group1" ], "exclude_organization_unit": [ "organization_unit1" ], "source_ip": [ "1.1.1.1" ] }, "destination": { "application": [ "application1" ], "app_suite": [ "appsuite1" ], "app_category": [ "category1" ], "web_category": [ "web_category1" ] }, "order": 1, "traffic_class": "Video" } ]
#services_client.update_bandwidth_control_traffic_class_rules(data, display_output=True) # Update bandwidth control traffic class rules. <---payload---> [ { "id": 1, "source": { "user": [ "user1" ], "user_group": [ "user_group1" ], "organization_unit": [ "organization_unit1" ], "exclude_user": [ "user1" ], "exclude_user_group": [ "user_group1" ], "exclude_organization_unit": [ "organization_unit1" ], "source_ip": [ "1.1.1.1" ] }, "destination": { "application": [ "application1" ], "app_suite": [ "appsuite1" ], "app_category": [ "category1" ], "web_category": [ "web_category1" ] }, "traffic_class": "Video" } ]
#services_client.list_bandwidth_control_traffic_class_rules(data, display_output=True) # Get bandwidth control traffic class rule list. <---payload---> { "filters": { "user": { "value": "User1", "operator": "like" }, "user_group": { "value": [ "UserGroup1" ] }, "organization_unit": { "value": [ "OU1" ] }, "source_ip": { "value": [ "SourceIP1" ] }, "application": { "value": "App1", "operator": "like" }, "app_suite": { "value": "AppSuite1", "operator": "like" }, "category": { "value": [ "Category1" ] }, "traffic_class": { "value": [ "Class1" ] } } }
#services_client.delete_bandwidth_control_traffic_class_rules(data, display_output=True) # Delete bandwidth control traffic class rules. <---payload---> [ 1 ]
#services_client.get_bandwidth_control_traffic_class_rule(rule_id, display_output=True) # Get bandwidth control traffic class rule.
#services_client.update_bandwidth_control_traffic_class_rule(rule_id, data, display_output=True) # Update a bandwidth control traffic class rule. <---payload---> { "source": { "user": [ "user1" ], "user_group": [ "user_group1" ], "organization_unit": [ "organization_unit1" ], "exclude_user": [ "user1" ], "exclude_user_group": [ "user_group1" ], "exclude_organization_unit": [ "organization_unit1" ], "source_ip": [ "1.1.1.1" ] }, "destination": { "application": [ "application1" ], "app_suite": [ "appsuite1" ], "app_category": [ "category1" ], "web_category": [ "web_category1" ] }, "order": 1, "traffic_class": "Video" }
#services_client.delete_bandwidth_control_traffic_class_rule(rule_id, display_output=True) # Delete a bandwidth control traffic class rule.

"""
UBA Data Scv Endpoint Testing
"""
#ubadatasvc_client.repeatable_demo(data, display_output=True) # Commands the repeatable demo app to populate the UEBA system with demo data and notfifications. <---payload---> { "userReplacements": [ { "baselineUser": "string", "demoUser": "string" } ] }
#ubadatasvc_client.user_uci(data, display_output=True) # Get single user's confidence index. <---payload---> { "user": "string", "fromTime": 0 }
