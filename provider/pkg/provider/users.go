package provider

import (
	"bytes"
	"encoding/json"
	fwRest "github.com/cloudy-sky-software/pulumi-provider-framework/rest"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/logging"
	pulumirpc "github.com/pulumi/pulumi/sdk/v3/proto/go"
	"io"
	"net/http"
	"net/url"
)

type staMgrBody struct {
	Cmd  string   `json:"cmd"`
	Macs []string `json:"macs"`
}

func deleteUser(deleteRequest *pulumirpc.DeleteRequest, httpReq *http.Request, provider *fwRest.Provider) error {
	// users are deleted using the `stamgr` command endpoint rather than through the standard DELETE rest endpoint
	mac := deleteRequest.OldInputs.AsMap()["mac"]
	logging.V(3).Infof("Using stamgr to delete the user %s", mac)

	httpReq.Method = "POST"
	stamgrUrl, err := url.Parse(provider.GetBaseURL() + "/api/s/default/cmd/stamgr")
	if err != nil {
		return err
	}
	httpReq.URL = stamgrUrl

	body := &staMgrBody{
		Cmd:  "forget-sta",
		Macs: []string{mac.(string)},
	}
	reqBody, _ := json.Marshal(body)
	var buf io.Reader
	buf = bytes.NewBuffer(reqBody)
	httpReq.Body = io.NopCloser(buf)

	return nil
}
