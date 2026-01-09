<script>
    let { data } = $props();

    import ProviderNav from "$lib/components/provider/ProviderNav.svelte";
    import ProviderContainer from "$lib/components/provider/ProviderContainer.svelte";
    import ProviderSingleRFQ from "$lib/components/provider/ProviderSingleRFQ.svelte";
</script>

<h1>{data.rfqid}</h1>

<div>
    <ProviderContainer>
        <ProviderNav />
        <ProviderSingleRFQ rfqid={data.rfqid}/>
    </ProviderContainer>
</div>
