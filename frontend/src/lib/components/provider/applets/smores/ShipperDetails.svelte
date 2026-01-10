<script lang="ts">
    let { quotedata } = $props();
</script>

<div
    class="flex flex-col gap-3 w-full bg-stone-100 border-stone-300 border-2 p-3 text-stone-700 rounded-2xl"
>
    <div class="font-bold text-xl">
        <span>Shipper Details</span>
    </div>

    <div class="font-bold text-lg text-stone-800">
        {quotedata.companyName}
    </div>
    <hr class="border-stone-300" />

    <div class="flex flex-col">
        <div class="text-sm stone-300">Email : {quotedata.email}</div>
        <div class="text-sm stone-300">Phone : {quotedata.phone}</div>
    </div>
</div>
